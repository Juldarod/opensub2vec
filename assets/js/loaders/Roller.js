import React from 'react';

const Roller = () => {
    return (
        <div
            style={{
                height: '100%',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            <div class="loader">
                <span />
                <span />
                <span />
            </div>
        </div>
    );
};

export default Roller;
