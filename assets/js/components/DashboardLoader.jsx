import React from 'react';
import Gear from '../loaders/Gear.jsx';

const DashboardLoader = () => {
    return (
        <div
            className="block"
            style={{
                height: '100vh',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            <Gear />
            <label style={{ color: 'rgba(205, 205, 205, 0.98)' }}>
                Loading models...
            </label>
        </div>
    );
};

export default DashboardLoader;
