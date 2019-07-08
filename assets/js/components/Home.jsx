import React from 'react';
import { Container, Segment } from 'semantic-ui-react';
import axios from 'axios';

class Home extends React.Component {
    state = {
        backendStatus: '',
    };

    componentDidMount() {
        axios
            .get('http://localhost:5000')
            .then(response => {
                console.log(response);
                this.setState({ backendStatus: response.data.message });
            })
            .catch(error => console.log(error.response.data));
    }

    render() {
        return (
            <Container id="hello">
                <Segment>{this.state.backendStatus}</Segment>
            </Container>
        );
    }
}

export default Home;
