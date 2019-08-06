import React, { Component } from 'react';
import axios from 'axios';
import DashboardLoader from './DashboardLoader.jsx';
import DashboardContent from './DashboardContent.jsx';
import SentenceTab from './SentenceTab.jsx';
import WordTab from './WordTab.jsx';

const panes = [
    {
        menuItem: 'Words',
        render: () => <WordTab />,
    },
    {
        menuItem: 'Sentences',
        render: () => <SentenceTab />,
    },
];

class Dashboard extends Component {
    state = {
        modelLoaded: true,
    };

    componentDidMount() {
        const { model } = this.props.match.params;

        // axios
        //   .get(`http://localhost:5000/model/load/${model}`)
        //   .then(response => {
        //     // console.log(response);
        //     this.setState({ modelLoaded: true });
        //   })
        //   .catch(error => console.log(error.response));
    }

    render() {
        return this.state.modelLoaded ? (
            <DashboardContent panes={panes} />
        ) : (
            <DashboardLoader />
        );
    }
}

export default Dashboard;
