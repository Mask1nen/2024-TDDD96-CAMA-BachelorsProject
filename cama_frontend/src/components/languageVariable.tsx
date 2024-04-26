
import React, { createContext, useState } from 'react';


export const value2 = createContext(true);

export default value2;
{/*
*/}

{/*
import React, { createContext, useState } from 'react';

// Create a new context
const SharedStateContext = createContext(true);

// Create a provider component
export const SharedStateProvider = ({ children }) => {
    const [value, setValue] = useState(true);
    
    return (
        <SharedStateContext.Provider value={{ value, setValue }}>
            {children}
        </SharedStateContext.Provider>
    );
    
};

export default SharedStateContext;
*/}

//export default SharedStateContext;

{/*
// Create a new context
const SharedStateContext = createContext(false);

// Create a provider component
export const SharedStateProvider = ({ children }) => {
    const [value, setValue] = useState(false);

    return (
        <SharedStateContext.Provider value={{ value, setValue }}>
            {children}
        </SharedStateContext.Provider>
    );
};


export default SharedStateContext;

const globalState = {
    value: false
};

export default globalState;
*/}