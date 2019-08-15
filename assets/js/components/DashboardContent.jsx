import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { Container, Menu, Tab } from 'semantic-ui-react';
import About from './Navbar/About.jsx';
import Contact from './Navbar/Contact.jsx';

const DashboardContent = ({ panes }) => {
    return (
        <Fragment>
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
                <Tab
                    id="tabs"
                    menu={{
                        size: 'massive',
                        secondary: true,
                        pointing: true,
                        inverted: true,
                    }}
                    panes={panes}
                />
            </Container>
        </Fragment>
    );
};

export default DashboardContent;
