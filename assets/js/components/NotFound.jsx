import React from 'react';
import { Segment, Container } from 'semantic-ui-react';

const NotFound = () => {
    return (
        <Container>
            <Segment id="not-found" placeholder>
                URL not found
            </Segment>
        </Container>
    );
};

export default NotFound;
