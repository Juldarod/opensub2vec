import React from 'react';
import {
    Tab,
    Segment,
    Grid,
    Divider,
    Icon,
    Input,
    Button,
} from 'semantic-ui-react';
import PlottingSegment from './PlottingSegment.jsx';

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
                <Grid columns={2} relaxed="very">
                    <Grid.Column>
                        <Input placeholder={'English'}>
                            <input />
                            <Button icon>
                                <Icon name="play" />
                            </Button>
                        </Input>
                    </Grid.Column>
                    <Grid.Column>
                        <Input placeholder={'Possible spanish translation'} />
                    </Grid.Column>
                </Grid>
                <Divider vertical>
                    <Icon name="picture" />
                </Divider>
            </Segment>
        </Tab.Pane>
    );
};

export default SentenceTab;
