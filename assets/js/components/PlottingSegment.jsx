import React from 'react';
import {
    Segment,
    Grid,
    Input,
    Button,
    Icon,
    Transition,
    Image,
    Divider,
} from 'semantic-ui-react';

const PlottingSegment = props => {
    const { model, onSearchChange, onSearchClick, visible, input } = props;

    return (
        <React.Fragment>
            <Grid.Column>
                <Input placeholder={model} onChange={e => onSearchChange(e)}>
                    <input />
                    <Button icon onClick={() => onSearchClick()}>
                        <Icon name="play" />
                    </Button>
                </Input>
                <Transition
                    visible={visible}
                    animation="horizontal flip"
                    duration={500}
                >
                    <Segment>
                        <Image src={`http://localhost:5000/plot/en/${input}`} />
                    </Segment>
                </Transition>
            </Grid.Column>
        </React.Fragment>
    );
};

export default PlottingSegment;
