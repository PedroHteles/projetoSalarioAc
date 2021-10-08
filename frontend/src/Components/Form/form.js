import React from 'react';

export const Form = ({ userInput, onFormChange, onFormSubmit, userInput1,onFormChange1 }) => {

    const handleChange = (event) =>{
        onFormChange(event.target.value)
    }
    const handleChange1 = (event) =>{
        onFormChange1(event.target.value)
    }

    const handleSubmit = (event) =>{
        event.preventDefault()
        onFormSubmit()
    }

    return(
        <>
        <form onSubmit={handleSubmit}>
            <input type='text' required value={userInput} onChange={handleChange}></input>
            <input type='text' required value={userInput1} onChange={handleChange1}></input>
            <input type='submit'></input>
        </form>
            
        </>
    )
}