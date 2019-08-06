import React, { Component } from 'react';
import {
    Segment,
    Grid,
    Input,
    Button,
    Icon,
    Transition,
    Image,
} from 'semantic-ui-react';

class PlottingSegment extends Component {
    state = {
        visible: false,
        tmpInput: '',
        input: '',
    };

    onSearchChange = e => {
        this.setState({ tmpInput: e.target.value });
    };

    onSearchClick = async () => {
        await this.setState({ visible: false });
        await this.setState({
            input: this.state.tmpInput,
        });
        await this.setState({ visible: true });
    };

    render() {
        const { model } = this.props;
        const { visible, input } = this.state;
        let lang = '';
        model == 'English' ? (lang = 'en') : (lang = 'es');

        return (
            <Grid.Column>
                <Input
                    placeholder={model}
                    onChange={e => this.onSearchChange(e)}
                >
                    <input />
                    <Button icon onClick={() => this.onSearchClick()}>
                        <Icon name="play" />
                    </Button>
                </Input>
                <Transition
                    visible={visible}
                    animation="horizontal flip"
                    duration={500}
                >
                    <Segment>
                        <Image
                            src={`http://localhost:5000/plot/${lang}/${input}`}
                        />
                    </Segment>
                </Transition>
            </Grid.Column>
        );
    }
}

export default PlottingSegment;
