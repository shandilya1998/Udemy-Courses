import React from "react";

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

export default Book;
