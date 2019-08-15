import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { Container, Segment, Popup, Icon, Menu } from 'semantic-ui-react';

import Models from './Navbar/Models.jsx';
import About from './Navbar/About.jsx';
import Contact from './Navbar/Contact.jsx';

const Home = () => {
    return (
        <Fragment>
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
        </Fragment>
    );
};

export default Home;
