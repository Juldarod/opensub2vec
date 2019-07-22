import React from 'react';
import { Transition } from 'semantic-ui-react';

class Gear extends React.Component {
    state = { visible: false };

    componentDidMount() {
        this.setState({ visible: true });
    }

    render() {
        return (
            <Transition
                duration={500}
                animation="zoom"
                visible={this.state.visible}
            >
                <div className="gear" />
            </Transition>
        );
    }
}

export default Gear;
