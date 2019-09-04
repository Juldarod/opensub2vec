import React from 'react';
import { Modal, Header } from 'semantic-ui-react';

const Contact = props => {
    return (
        <Modal dimmer={'blurring'} trigger={props.trigger}>
            <Header icon="address book" content="Contact" />
            <Modal.Content>
                <h3>Github repository</h3>
                <p>https://juldarod.github.com/opensub2vec</p>
            </Modal.Content>
        </Modal>
    );
};

export default Contact;
