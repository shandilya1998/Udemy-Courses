import React from 'react';
import ReactDOM from 'react-dom';


// Component name must be caplitalised
// Stateless Functional Component
function Greeting(){
    return (
        <div>
            <h1>Hello World!</h1>
        </div>
    );
}

ReactDOM.render(
    <Greeting/>, document.getElementById('root')
);
