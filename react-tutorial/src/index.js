import React from 'react';
import ReactDOM from 'react-dom';


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

// SETUP
const books = [
    {
        key: 0,
        title: 'The Psychology of Money',
        author: 'Morgan Housel',
        src: 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg'
    }, {
        key: 1,
        title: 'Ikigai: The Japanese secret to a long and happy life',
        src: 'https://images-eu.ssl-images-amazon.com/images/I/81l3rZK4lnL._AC_UL604_SR604,400_.jpg',
        author: 'Héctor García'
    }, {
        key: 2,
        title: 'DO EPIC SHIT',
        author: 'Ankur Warikoo',
        src: 'https://images-eu.ssl-images-amazon.com/images/I/41+grDTP2FL._AC_UL604_SR604,400_.jpg'
    }, {
        key: 3,
        title: 'Atomic Habits: The life-changing million copy bestseller',
        author: 'James Clear',
        src: 'https://images-eu.ssl-images-amazon.com/images/I/51S7KOWir7L._AC_UL604_SR604,400_.jpg'
    }
];

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

const Book = (props) => {
    const {src, title, author} = props;
    const clickHandler = (event) => {
        console.log(event);
        alert('hello world');
    };
    const clickHandler2 = (author) => {
        alert(author);
    };
    return (
        <article className="book" onMouseOver={() => {
            console.log(title);
        }}>
            <img src={src} alt=''></img>
            <h1 onClick={() => {alert(title)}} >{title}</h1>    
            <h4 style={{
                color: '#617d98',
                fontSize: '0.75rem',
                margin: '0.25rem'
                }}>
                    {author}
            </h4>
            <button type='button' onClick={clickHandler}>
                Test Button 1
            </button>
            <button type='button' onClick={()=>{clickHandler2(author)}}>
                Test Button 2
            </button>
        </article>
    );
};


ReactDOM.render(
    <Booklist />, document.getElementById('root')
);
