import React, { useState, Fragment } from 'react';
import {
    Transition,
    Segment,
    Input,
    Button,
    Icon,
    Grid,
    Checkbox,
    Dimmer,
} from 'semantic-ui-react';
import axios from 'axios';

import PlotAndTable from '../PlotAndTable.jsx';

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
        const lang = toggle ? 'en' : 'es';

        const phrases = await axios
            .get(`http://localhost:5000/phraser/${lang}/${tmpInput}`)
            .then((res) => res.data.phrases);

        axios
            .get(`http://localhost:5000/mostsimilar/${lang}/${phrases}`)
            .then((res) => {
                setSimilars(res.data.result);
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
        setToggle((prevState) => !prevState);
        setSimilars([]);
    };

    return (
        <Segment>
            <Grid.Row>
                <Grid columns={2}>
                    <Grid.Column widescreen={14}>
                        <Input
                            placeholder={toggle ? 'English' : 'Spanish'}
                            onChange={(e) => setTmpInput(`${e.target.value}`)}
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
                        </Input>
                    </Grid.Column>
                    <Grid.Column widescreen={2}>
                        <Checkbox toggle onChange={() => onCheckboxChange()} />
                    </Grid.Column>
                </Grid>
            </Grid.Row>
            <Grid.Row>
                {/* <Transition.Group
                    // visible={visible}
                    // animation="horizontal flip"
                    // duration={500}
                >
                    {similars.length !== 0 ? ( */}
                        <PlotAndTable
                            input={input}
                            similars={similars}
                            toggle={toggle}
                        />
                    {/* ) : (
                        <></>
                    )}
                </Transition.Group> */}
            </Grid.Row>
        </Segment>
    );
};

export default Similarity;
