import React from 'react';
import { Tab } from 'semantic-ui-react';

import Similarity from './Similarity.jsx';
// import Similarity from './SimilarityCopy.jsx';
import Analogy from './Analogy.jsx';

const WordTab = () => {
    return (
        <Tab.Pane>
            <h3>Similarity</h3>
            <Similarity />
            <h3>Analogy</h3>
            <Analogy />
        </Tab.Pane>
    );
};

export default WordTab;
