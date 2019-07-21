import React from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import Home from './Home.jsx';
import Dashboard from './Dashboard.jsx';
import NotFound from './NotFound.jsx';

const Router = () => {
    return (
        <HashRouter>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/dashboard" component={Dashboard} />
                <Route component={NotFound} />
            </Switch>
        </HashRouter>
    );
};

export default Router;
