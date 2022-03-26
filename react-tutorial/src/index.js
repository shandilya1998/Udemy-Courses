import React from 'react';
import ReactDOM from 'react-dom';

import {books} from './books';
import Book from './book';

// CSS
import './index.css';

// Component name must be caplitalised
// Stateless Functional Component
// A component must always return JSX
// A component must return a single component
// `div`, `section` or `React.Fragment` (<></>) must be the root parent of JSX tree
// Follow HTML semantics
// Use camelcase for html attributes
// `class` attribute is replaced with `className`
// Every elemt must be closed

/*
const Greeting = () => {
    return React.createElement(
        'h1',
        {},
        'Hello World!'
    );
};
*/

function Booklist(){
    return (
        <section className="booklist">
            {
                books.map(
                    (book) => <Book {...book} />
                )
            }
        </section>
    );
}


ReactDOM.render(
    <Booklist />, document.getElementById('root')
);
