import React from 'react';
import { Modal, Header } from 'semantic-ui-react';

const Models = props => {
    return (
        <Modal dimmer={'blurring'} trigger={props.trigger}>
            <Header icon="cogs" content="Models" />
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

export default Models;
