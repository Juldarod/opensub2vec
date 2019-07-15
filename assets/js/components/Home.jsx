import React, { Fragment } from 'react';
import { Button, Checkbox, Icon } from 'semantic-ui-react';
import axios from 'axios';

class Home extends React.Component {
    state = {
        backendStatus: '',
        activeItem: '',
    };

    // componentDidMount() {
    //     axios
    //         .get('http://localhost:5000')
    //         .then(response => {
    //             console.log(response);
    //             this.setState({ backendStatus: response.data.message });
    //         })
    //         .catch(error => console.log(error.response.data));
    // }

    handleCheckboxChange = (e, { value }) => this.setState({ value });

    render() {
        const { activeItem } = this.state;

        return (
            <Fragment>
                <div id="home-menu">
                    <label>Models</label>
                    <label>About</label>
                    <label>Contact</label>
                </div>
                <div id="landing">
                    <h1>Opensub2Vec</h1>
                    <div id="model-selection">
                        <label>Select a model</label>
                        <Checkbox
                            radio
                            label="Word2vec"
                            name="checkboxRadioGroup"
                            value="this"
                            checked={this.state.value === 'this'}
                            onChange={this.handleCheckboxChange}
                        />
                        <Checkbox
                            radio
                            label="fastText"
                            name="checkboxRadioGroup"
                            value="that"
                            checked={this.state.value === 'that'}
                            onChange={this.handleCheckboxChange}
                        />
                        <Button animated>
                            <Button.Content visible>Go!</Button.Content>
                            <Button.Content hidden>
                                <Icon name="arrow right" />
                            </Button.Content>
                        </Button>
                    </div>
                </div>
            </Fragment>
        );
    }
}

export default Home;
