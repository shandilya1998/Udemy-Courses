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

function Booklist(){
    return (
        <section>
            <Book />
            <Book />
            <Book />
            <Book />
            <Book />
            <Book />
            <Book />
        </section>
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

const Book = () => {
    return (
        <article>
            <Image />
            <Title />
            <Author />
        </article>
    );
};

// Implicit Return
const Image = () => <img 
    src='https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg' alt=''></img>;

// Explicit Return
const Title = () => {
    return (
        <h1>The Psychology of Money</h1>
    );
};


const Author = () => <h4>Morgan Housel</h4>;

ReactDOM.render(
    <Booklist />, document.getElementById('root')
);
