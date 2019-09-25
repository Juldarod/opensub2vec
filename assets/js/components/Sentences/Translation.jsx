import React, { Component, Fragment } from 'react';
import {
    Grid,
    Input,
    Button,
    Icon,
    Transition,
    Segment,
    Image,
    Divider,
    Table,
} from 'semantic-ui-react';
import axios from 'axios';
import _ from 'lodash';

// ( "" ) -> [{}, ..., {}]
const translate = async sentence => {
    console.log('Beginning translation...');

    const translation = await axios
        .get(`http://localhost:5000/translate/${sentence}`)
        .then(res => {
            console.log(res.data);
            return res.data.result;
        })
        .catch(error => console.log(error.response));

    return translation;
};

// ( [[], ..., []] ) -> ""
const getTranslatedWords = async vectors => {
    const words = _.concat(...vectors[1], ...vectors[2]);
    // const words = vectors[1];
    return words.join(' ');
};

// ( "", [ [], ..., [] ] ) -> []
const calclWmdistances = async (source, target) => {
    console.log(target);

    const wmdistances = await Promise.all(
        target.map(async sentence => {
            const translatedSentence = await axios
                .get(
                    `http://localhost:5000/wmdistance/${source}/${sentence.join(
                        ' '
                    )}`
                )
                .then(res => {
                    return res.data.result;
                });

            return translatedSentence;
        })
    );

    console.log(wmdistances);

    return wmdistances;
};

export default class Translation extends Component {
    state = {
        buttonLoading: false,
        visible: true,
        wmvisible: false,
        tmpEnInput: '',
        tmpSpInput: '',
        enInput: '',
        spInput: '',
        withoutStopwords: '',
        words: '',

        translatedSentences: [],
        wmdistances: [],

        image: 'https://react.semantic-ui.com/images/wireframe/image.png',
    };

    onEnglishChange = e => {
        this.setState({ tmpEnInput: e.target.value });
    };

    onSpanishChange = e => {
        this.setState({ tmpSpInput: e.target.value });
    };

    onPlayClick = async () => {
        await this.setState({ buttonLoading: true });
        const phrases_en = await axios
            .get(`http://localhost:5000/phraser/en/${this.state.tmpEnInput}`)
            .then(res => {
                return res.data.phrases;
            });
        const es_non_stop = await axios
            .get(`http://localhost:5000/remove/es/${this.state.tmpSpInput}`)
            .then(res => res.data.result.join(' '));
        const phrases_es = await axios
            .get(`http://localhost:5000/phraser/es/${es_non_stop}`)
            .then(res => {
                return res.data.phrases;
            });
        await this.setState({
            enInput: phrases_en,
            spInput: phrases_es,
        });

        const translatedWords = await translate(this.state.enInput);
        const sentences = translatedWords.map(translation => [
            translation.original,
            ...translation.translations,
        ]);
        const newSent = _.zip(...sentences);

        await this.setState({
            translatedSentences: _.tail(newSent).map(sent => sent.join(' ')),
        });
        console.log(newSent);

        const words = await getTranslatedWords(newSent);
        await this.setState({ visible: false });
        await this.setState({ withoutStopwords: _.first(newSent).join(' ') });
        await this.setState({ words });
        await this.setState({
            image: `http://localhost:5000/plot/translation/${this.state.withoutStopwords}/${this.state.words}`,
        });
        await this.setState({ visible: true });

        const wmdistances = await calclWmdistances(
            this.state.spInput,
            _.tail(newSent)
        );
        await this.setState({ wmdistances });
        await this.setState({ wmvisible: true });
        await this.setState({ buttonLoading: false });
    };

    render() {
        return (
            <Fragment>
                <Segment>
                    <Grid columns={2} relaxed="very">
                        <Grid.Column>
                            <Input
                                placeholder={'English'}
                                onChange={e => this.onEnglishChange(e)}
                            >
                                <input />
                                <Button
                                    loading={this.state.buttonLoading}
                                    icon
                                    onClick={() => this.onPlayClick()}
                                >
                                    <Icon name="play" />
                                </Button>
                            </Input>
                        </Grid.Column>
                        <Grid.Column>
                            <Input
                                placeholder={'Possible spanish translation'}
                                onChange={e => this.onSpanishChange(e)}
                            />
                        </Grid.Column>
                    </Grid>
                    <Divider vertical>
                        <Icon name="picture" />
                    </Divider>
                </Segment>
                <Transition
                    visible={this.state.visible}
                    animation="horizontal flip"
                    duration={500}
                >
                    <Segment>
                        <Image
                            src={this.state.image}
                            centered
                            style={{ width: '70%' }}
                        />
                    </Segment>
                </Transition>
                <Transition
                    visible={this.state.wmvisible}
                    animation="horizontal flip"
                    duration={500}
                >
                    <Segment>
                        <Table basic="very" celled>
                            <Table.Header>
                                <Table.Row>
                                    <Table.HeaderCell>Initial</Table.HeaderCell>
                                    <Table.HeaderCell>
                                        Translated
                                    </Table.HeaderCell>
                                    <Table.HeaderCell>Score</Table.HeaderCell>
                                </Table.Row>
                            </Table.Header>
                            <Table.Body>
                                <Table.Row>
                                    <Table.Cell>
                                        {this.state.spInput}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.translatedSentences[0]}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.wmdistances[0]}
                                    </Table.Cell>
                                </Table.Row>
                                <Table.Row>
                                    <Table.Cell>
                                        {this.state.spInput}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.translatedSentences[1]}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.wmdistances[1]}
                                    </Table.Cell>
                                </Table.Row>
                                <Table.Row>
                                    <Table.Cell>
                                        {this.state.spInput}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.translatedSentences[2]}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.wmdistances[2]}
                                    </Table.Cell>
                                </Table.Row>
                                <Table.Row>
                                    <Table.Cell>
                                        {this.state.spInput}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.translatedSentences[3]}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.wmdistances[3]}
                                    </Table.Cell>
                                </Table.Row>
                                <Table.Row>
                                    <Table.Cell>
                                        {this.state.spInput}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.translatedSentences[4]}
                                    </Table.Cell>
                                    <Table.Cell>
                                        {this.state.wmdistances[4]}
                                    </Table.Cell>
                                </Table.Row>
                            </Table.Body>
                        </Table>
                        {/* {this.state.spInput} vs{' '}
                        {this.state.translatedSentences[0]} ={' '}
                        {this.state.wmdistances[0]}
                        <br />
                        {this.state.spInput} vs{' '}
                        {this.state.translatedSentences[1]} ={' '}
                        {this.state.wmdistances[1]}
                        <br />
                        {this.state.spInput} vs{' '}
                        {this.state.translatedSentences[2]} ={' '}
                        {this.state.wmdistances[2]}
                        <br />
                        {this.state.spInput} vs{' '}
                        {this.state.translatedSentences[3]} ={' '}
                        {this.state.wmdistances[3]}
                        <br />
                        {this.state.spInput} vs{' '}
                        {this.state.translatedSentences[4]} ={' '}
                        {this.state.wmdistances[4]} */}
                    </Segment>
                </Transition>
            </Fragment>
        );
    }
}
