import React, { Component, Fragment } from 'react';
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

import blankPicture from '../../../static/blankpicture.png';
import blankParagraph from '../../../static/blankParagraph.png';
import blankShortParagraph from '../../../static/blankShortParagraph.png';
import axios from 'axios';

export default class Similarity extends Component {
    state = {
        buttonLoading: false,
        tmpInput: '',
        input: '',
        toggle: true,
        visible: true,
        lang: 'English',
        similars: [],
    };

    onSearchChange = e => {
        this.setState({ tmpInput: e.target.value });
    };

    onSearchClick = async () => {
        this.setState({ buttonLoading: true });
        this.setState({ similars: [] });
        const lang = this.state.toggle ? 'english' : 'spanish';
        const phrases = await axios
            .get(`http://localhost:5000/phraser/${lang}/${this.state.tmpInput}`)
            .then(res => {
                return res.data.phrases;
            });
        this.setState({ input: phrases });

        await axios
            .get(
                `http://localhost:5000/mostsimilar/${
                this.state.toggle ? 'en' : 'es'
                }/${this.state.input}`
            )
            .then(async res => {
                // console.log(res.data.result);
                await this.setState({ similars: res.data.result });
            });
        this.setState({ visible: false });
        this.setState({ visible: true });
        this.setState({ buttonLoading: false });
    };

    onCheckboxChange = async () => {
        this.setState(prevState => {
            return { toggle: !prevState.toggle };
        });
        this.setState({ similars: [] });
    };

    render() {
        return (
            <Segment>
                <Grid columns={2} relaxed="very">
                    <Grid.Column verticalAlign="middle">
                        <Input
                            placeholder={
                                this.state.toggle ? 'English' : 'Spanish'
                            }
                            onChange={e => this.onSearchChange(e)}
                        >
                            <input />
                            <Button
                                loading={this.state.buttonLoading}
                                icon
                                onClick={() => this.onSearchClick()}
                            >
                                <Icon name="play" />
                            </Button>
                            <Checkbox
                                toggle
                                onChange={() => this.onCheckboxChange()}
                            />
                        </Input>
                        {/* <Transition
                            visible={this.state.visible}
                            animation="horizontal flip"
                            duration={500}
                        > */}
                        <Segment>
                            {this.state.similars.length == 0 ? (
                                <p>
                                    <Image src={blankPicture} />
                                </p>
                            ) : (
                                    <p>
                                        <Image
                                            src={`http://localhost:5000/plot/${
                                                this.state.toggle ? 'en' : 'es'
                                                }/${
                                                this.state.input
                                                } ${this.state.similars
                                                    .map(el => el[0])
                                                    .join(' ')}`}
                                        />
                                    </p>
                                )}
                        </Segment>
                        {/* </Transition> */}
                    </Grid.Column>
                    <Grid.Column verticalAlign="middle">
                        {/* <Transition
                            visible={this.state.visible}
                            animation="horizontal flip"
                            duration={500}
                        > */}
                        <Segment>
                            {this.state.similars.length == 0 ? (
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
                                            {this.state.similars.map(el => (
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
                        {/* </Transition> */}
                    </Grid.Column>
                </Grid>
            </Segment>
        );
    }
}
