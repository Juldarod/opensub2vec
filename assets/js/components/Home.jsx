import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { Container, Segment, Popup, Icon, Menu } from 'semantic-ui-react';

import Models from './Models.jsx';
import About from './About.jsx';
import Contact from './Contact.jsx';

const Home = () => {
    return (
        <React.Fragment>
            <Container id="home-menu">
                <Menu secondary>
                    <Models trigger={<Menu.Item name="Models" />} />
                    <Menu.Menu position="right">
                        <About trigger={<Menu.Item name="About" />} />
                        <Contact trigger={<Menu.Item name="Contact" />} />
                    </Menu.Menu>
                </Menu>
            </Container>
            <Container id="landing">
                <h1>Opensub2Vec</h1>

                <label>
                    Select a model
                    <Popup
                        position="top center"
                        content="Click on models menu for more information"
                        trigger={<Icon name="question circle" />}
                    />
                </label>
                <Container id="model-selection">
                    <div>
                        <Link to="/word2vec">
                            <Segment circular inverted>
                                word2vec
                            </Segment>
                        </Link>
                        <Link to="/fasttext">
                            <Segment circular inverted>
                                fastText
                            </Segment>
                        </Link>
                    </div>
                </Container>
            </Container>
        </React.Fragment>
    );
};

export default Home;
