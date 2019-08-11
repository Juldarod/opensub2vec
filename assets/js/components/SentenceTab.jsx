import React from 'react';
import { Tab, Segment, Grid, Divider, Icon } from 'semantic-ui-react';
import PlottingSegment from './PlottingSegment.jsx';
import Translation from './Translation.jsx';

const SentenceTab = () => {
    return (
        <Tab.Pane>
            {}
            <h3>Plotting</h3>
            <Segment>
                <Grid columns={2} relaxed="very">
                    <PlottingSegment model={'English'} />
                    <PlottingSegment model={'Spanish'} />
                </Grid>
                <Divider vertical>
                    <Icon name="picture" />
                </Divider>
            </Segment>
            {}
            <h3>Translation</h3>
            <Segment>
                <Translation />
            </Segment>
        </Tab.Pane>
    );
};

export default SentenceTab;
