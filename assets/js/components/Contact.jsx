import React from 'react';
import { Modal, Header } from 'semantic-ui-react';

const Contact = props => {
    return (
        <Modal
            dimmer={'blurring'}
            /* centered={false} */ trigger={props.trigger}
        >
            <Header icon="address book" content="Contact" />
            <Modal.Content>
                <p>
                    Your inbox is getting full, would you like us to enable
                    automatic archiving of old messages? Your inbox is getting
                    full, would you like us to enable automatic archiving of old
                    messages?
                </p>
            </Modal.Content>
        </Modal>
    );
};

export default Contact;
