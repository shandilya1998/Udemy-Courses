import React from 'react';
import ReactDOM from 'react-dom';


// Component name must be caplitalised
// Stateless Functional Component
// A component must always return JSX
// A component must return a single component
// `div`, `section` or `React.Fragment` (<></>) must be the root parent of JSX tree
// Follow HTML semantics
// Use camelcase for html attributes
// `class` attribute is replaced with `className`
// Every elemt must be closed

function Greeting(){
    return (
        <div>
            <h1>Hello World!</h1>
            <Person />
            <Message />
        </div>
    );
}

/*
const Greeting = () => {
    return React.createElement(
        'h1',
        {},
        'Hello World!'
    );
};
*/

// Implicit Return
const Person = () => <h3>Shreyas Shandilya</h3>;

// Explocit Return
const Message = () => {
    return (
        <p>This is my Message</p>
    );
};


ReactDOM.render(
    <Greeting />, document.getElementById('root')
);
