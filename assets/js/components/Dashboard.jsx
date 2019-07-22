import React from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Container, Segment, Menu } from 'semantic-ui-react';
import Gear from '../loaders/Gear';
// import Geometry from '../loaders/Geometry';
// import Roller from '../loaders/Roller';
import About from './About.jsx';
import Contact from './Contact.jsx';

class Dashboard extends React.Component {
    state = {
        loadedModel: true,
    };

    componentDidMount() {
        const { model } = this.props.match.params;

        // axios
        //     .get(`http://localhost:5000/model/load/${model}`)
        //     .then(response => {
        //         console.log(response);
        //         this.setState({ loadedModel: true });
        //     })
        //     .catch(error => console.log(error.response.data));
    }

    renderLoader = () => {
        return (
            <div
                className="block"
                style={{
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <Gear />
                <label style={{ color: 'rgba(205, 205, 205, 0.98)' }}>
                    Loading models...
                </label>
            </div>
        );
    };

    renderContent = () => {
        return (
            <React.Fragment>
                <Container id="home-menu">
                    <Menu secondary>
                        <Link to="/">
                            <Menu.Item name="Home" />
                        </Link>
                        <Menu.Menu position="right">
                            <About trigger={<Menu.Item name="About" />} />
                            <Contact trigger={<Menu.Item name="Contact" />} />
                        </Menu.Menu>
                    </Menu>
                </Container>
                <Container>
                    <Segment>most similar picture</Segment>
                    <Segment>analogies picture</Segment>
                    <Segment>sentences in both languages picture</Segment>
                    <Segment>
                        sentence translation picture: a sentence in english and
                        its translation in spanish
                    </Segment>
                    <Segment>
                        wmdistance between original spanish sentence and
                        translated sentences
                    </Segment>
                </Container>
            </React.Fragment>
        );
    };

    render() {
        return this.state.loadedModel
            ? this.renderContent()
            : this.renderLoader();
    }
}

export default Dashboard;
