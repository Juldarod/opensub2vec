import React from 'react';
import { Tab, Segment } from 'semantic-ui-react';

const WordTab = () => {
    return (
        <Tab.Pane>
            (Most Similar)
            <Segment>{}</Segment>
            (Analogies picture)
            <Segment>{}</Segment>
        </Tab.Pane>
    );
};

export default WordTab;
