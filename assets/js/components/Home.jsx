import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { Container, Segment, Popup, Icon, Menu } from 'semantic-ui-react';

import Models from './Models.jsx';
import About from './About.jsx';
import Contact from './Contact.jsx';

const Home = () => {
    return (
        <Fragment>
            <Container id="home-menu">
                <Menu secondary>
                    <Models trigger={<Menu.Item name=" Models" />} />
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
                        <Link to="/dashboard">
                            <Segment
                                vertical
                                circular
                                onClick={() => console.log('word2vec selected')}
                                inverted
                            >
                                word2vec
                            </Segment>
                        </Link>
                        <Link to="/dashboard">
                            <Segment
                                circular
                                onClick={() => console.log('fastText selected')}
                                inverted
                            >
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
