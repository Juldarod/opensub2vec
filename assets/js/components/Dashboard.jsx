import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import DashboardLoader from './DashboardLoader.jsx';
import DashboardContent from './DashboardContent.jsx';
import SentenceTab from './Sentences/SentenceTab.jsx';
import WordTab from './Words/WordTab.jsx';

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

const Dashboard = () => {
    const { model } = useParams();
    const [isModelLoaded, setIsModelLoaded] = useState(false);

    // useEffect(() => {
    //     axios
    //         .get(`http://localhost:5000/model/load/${model}`)
    //         .then((response) => {
    //             console.log(response);
    //             setIsModelLoaded(true);
    //         })
    //         .catch((error) => console.log(error.response));
    // }, []);

    return /* isModelLoaded */true ? (
        <DashboardContent panes={panes} />
    ) : (
        <DashboardLoader />
    );
};

export default Dashboard;
