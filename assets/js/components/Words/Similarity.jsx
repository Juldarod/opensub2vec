import React, { useState, Fragment } from 'react';
import {
    Transition,
    Segment,
    Input,
    Button,
    Icon,
    Image,
    Grid,
    Table,
    Header,
    Checkbox,
} from 'semantic-ui-react';
import axios from 'axios';

import blankPicture from '../../../static/blankpicture.png';
import blankParagraph from '../../../static/blankparagraph.png';
import blankShortParagraph from '../../../static/blankshortparagraph.png';
import axios from 'axios';

const Similarity = () => {
    const [tmpInput, setTmpInput] = useState('');
    const [input, setInput] = useState('');
    const [similars, setSimilars] = useState([]);
    const [toggle, setToggle] = useState(true);
    const [buttonLoading, setButtonLoading] = useState(false);
    const [visible, setVisible] = useState(true);

    const onSearchClick = async () => {
        setButtonLoading(true);
        setSimilars([]);
        const lang = toggle ? 'english' : 'spanish';

        const phrases = await axios
            .get(`http://localhost:5000/phraser/${lang}/${tmpInput}`)
            .then(res => res.data.phrases);

        axios
            .get(
                `http://localhost:5000/mostsimilar/${
                toggle ? 'en' : 'es'
                }/${phrases}`
            )
            .then(res => {
                setSimilars(res.data.result)
            });

        setInput(phrases);

        // axios.get(`http://localhost:5000/plot/${
        //     toggle ? 'en' : 'es'
        //     }/${
        //     input
        //     } ${similars
        //         .map(el => el[0])
        //         .join(' ')}`).then(res => console.log(res)
        //         )
    };

    const onCheckboxChange = () => {
        setToggle(prevState => !prevState)
        setSimilars([])
    };

    return (
        <Segment>
            <Grid columns={2} relaxed="very">
                <Grid.Column verticalAlign="middle">
                    <Input
                        placeholder={
                            toggle ? 'English' : 'Spanish'
                        }
                        onChange={e => setTmpInput(`${e.target.value}`)}
                    >
                        <input />
                        <Button
                            loading={buttonLoading}
                            icon
                            onClick={async () => {
                                await onSearchClick();
                                setVisible(false);
                                setButtonLoading(false);
                                setVisible(true);
                            }}
                        >
                            <Icon name="play" />
                        </Button>
                        <Checkbox
                            toggle
                            onChange={() => onCheckboxChange()}
                        />
                    </Input>
                    <Transition
                        visible={visible}
                        animation="horizontal flip"
                        duration={500}
                    >
                        <Segment>
                            {similars.length == 0 ? (
                                <p>
                                    <Image src={blankPicture} />
                                </p>
                            ) : (
                                    <p>
                                        <Image
                                            src={`http://localhost:5000/plot/${
                                                toggle ? 'en' : 'es'
                                                }/${
                                                input
                                                } ${similars
                                                    .map(el => el[0])
                                                    .join(' ')}`}
                                        />
                                    </p>
                                )}
                        </Segment>
                    </Transition>
                </Grid.Column>
                <Grid.Column verticalAlign="middle">
                    <Transition
                        visible={visible}
                        animation="horizontal flip"
                        duration={500}
                    >
                        <Segment>
                            {similars.length == 0 ? (
                                <Fragment>
                                    <p>
                                        <Image src={blankShortParagraph} />
                                    </p>
                                    <p>
                                        <Image src={blankParagraph} />
                                    </p>
                                    <p>
                                        <Image src={blankParagraph} />
                                    </p>
                                </Fragment>
                            ) : (
                                    <Table basic="very" celled>
                                        <Table.Header>
                                            <Table.Row>
                                                <Table.HeaderCell>
                                                    Word
                                            </Table.HeaderCell>
                                                <Table.HeaderCell>
                                                    Score
                                            </Table.HeaderCell>
                                            </Table.Row>
                                        </Table.Header>
                                        <Table.Body>
                                            {similars.map(el => (
                                                <Table.Row key={el[0]}>
                                                    <Table.Cell>
                                                        <Header as="h4" image>
                                                            <Header.Content>
                                                                {el[0]}
                                                            </Header.Content>
                                                        </Header>
                                                    </Table.Cell>
                                                    <Table.Cell>{el[1]}</Table.Cell>
                                                </Table.Row>
                                            ))}
                                        </Table.Body>
                                    </Table>
                                )}
                        </Segment>
                    </Transition>
                </Grid.Column>
            </Grid>
        </Segment>
    );
}

export default Similarity;