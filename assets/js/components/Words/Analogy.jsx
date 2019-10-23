import React, { Component, Fragment } from 'react';
import {
    Segment,
    Input,
    Label,
    Button,
    Icon,
    Image,
    Grid,
    Table,
    Header,
} from 'semantic-ui-react';
import axios from 'axios';

import blankPicture from '../../../static/blankpicture.png';
import blankParagraph from '../../../static/blankparagraph.png';

export default class Analogy extends Component {
    state = {
        input: '',
        input1: '',
        input2: '',
        input3: '',
        result: [],
        answer: '',
    };

    onSearchChange = (e, pos) => {
        if (pos == 1) {
            this.setState({ input1: e.target.value });
        }
        if (pos == 2) {
            this.setState({ input2: e.target.value });
        }
        if (pos == 3) {
            this.setState({ input3: e.target.value });
        }
    };

    onSearchClick = async () => {
        const phrases1 = await axios
            .get(`http://localhost:5000/phraser/en/${this.state.input1}`)
            .then(res => {
                return res.data.phrases;
            });
        const phrases2 = await axios
            .get(`http://localhost:5000/phraser/en/${this.state.input2}`)
            .then(res => {
                return res.data.phrases;
            });
        const phrases3 = await axios
            .get(`http://localhost:5000/phraser/en/${this.state.input3}`)
            .then(res => {
                return res.data.phrases;
            });
        await this.setState({
            input: `${phrases3} ${phrases2} ${phrases1}`,
        });
        await axios
            .get(`http://localhost:5000/analogy/en/${this.state.input}`)
            .then(async res => {
                console.log(res.data.result);
                await this.setState({
                    result: res.data.result,
                    answer: res.data.result[0][0],
                });
            });
    };

    render() {
        return (
            <Segment>
                <Segment style={{ display: 'flex' }}>
                    <Input
                        placeholder={'Test'}
                        onChange={e => this.onSearchChange(e, 1)}
                    />
                    <Label>is to</Label>
                    <Input
                        placeholder={'Test'}
                        onChange={e => this.onSearchChange(e, 2)}
                    />
                    <Label>as</Label>
                    <Input
                        placeholder={'Test'}
                        onChange={e => this.onSearchChange(e, 3)}
                    />
                    <Label>is to</Label>
                    <Input placeholder={this.state.answer}>
                        <input />
                        <Button icon onClick={() => this.onSearchClick()}>
                            <Icon name="play" />
                        </Button>
                    </Input>
                </Segment>
                <Grid columns={2}>
                    <Grid.Column verticalAlign="middle">
                        <Segment>
                            {this.state.result.length == 0 ? (
                                <p>
                                    <Image src={blankPicture} />
                                </p>
                            ) : (
                                <p>
                                    <Image
                                        src={`http://localhost:5000/plot/en/${
                                            this.state.input
                                        } ${this.state.result[0][0]}`}
                                    />
                                </p>
                            )}
                        </Segment>
                    </Grid.Column>
                    <Grid.Column verticalAlign="middle">
                        <Segment>
                            {this.state.result.length == 0 ? (
                                <Fragment>
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
                                        {this.state.result.map(el => (
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
                    </Grid.Column>
                </Grid>
            </Segment>
        );
    }
}
