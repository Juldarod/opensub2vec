import React from 'react';
import { HashRouter, Route, Routes } from 'react-router-dom';
import Home from './Home.jsx';
import Dashboard from './Dashboard.jsx';
import NotFound from './NotFound.jsx';

const Router = () => {
    return (
        <HashRouter>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/:model" element={<Dashboard />} />
                <Route element={<NotFound />} />
            </Routes>
        </HashRouter>
    );
};

export default Router;
