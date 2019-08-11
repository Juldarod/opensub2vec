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
} from 'semantic-ui-react';
import axios from 'axios';
import _ from 'lodash';

const translate = async sentence => {
    console.log('Beginning translation...');

    const translation = await axios
        .get(`http://localhost:5000/translate/${sentence}`)
        .then(res => res.data.words)
        .catch(error => console.log(error.response));

    return translation;
};

const getTranslatedWords = async vectors => {
    const words = _.concat(...vectors[1], ...vectors[2], ...vectors[3]);
    // const words = vectors[1];
    return words.join(' ');
};

export default class Translation extends Component {
    state = {
        visible: false,
        tmpEnInput: '',
        tmpSpInput: '',
        enInput: '',
        spInput: '',
        withoutStopwords: '',
        words: '',
    };

    onEnglishChange = e => {
        this.setState({ tmpEnInput: e.target.value });
    };

    onSpanishChange = e => {
        this.setState({ tmpSpInput: e.target.value });
    };

    onPlayClick = async () => {
        await this.setState({
            enInput: this.state.tmpEnInput,
            spInput: this.state.tmpSpInput,
        });

        const translatedWords = await translate(this.state.enInput);
        const sentences = translatedWords.map(translation => [
            translation.original,
            ...translation.translations,
        ]);
        const newSent = _.zip(...sentences);
        console.log(newSent);

        const words = await getTranslatedWords(newSent);
        await this.setState({ withoutStopwords: _.first(newSent).join(' ') });
        await this.setState({ words });
        await this.setState({ visible: true });
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
                                <Button icon onClick={() => this.onPlayClick()}>
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
                            src={`http://localhost:5000/plot/translation/${
                                this.state.withoutStopwords
                            }/${this.state.words}`}
                        />
                    </Segment>
                </Transition>
            </Fragment>
        );
    }
}
