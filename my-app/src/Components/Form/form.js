import React from 'react';
export const Form = ({ userInput, onFormChange, onFormSubmit, userInput1,onFormChange1 }) => {

    const handleSubmit = (event) =>{
        event.preventDefault()
        onFormSubmit()}
    return(
        <>
        <form onSubmit={handleSubmit}>
            <input type='number' required value={userInput} onChange={(e) => onFormChange(e.target.value)}></input>
            <input type='number' required value={userInput1} onChange={(e) => onFormChange1(e.target.value)}></input>
            <input type='submit'></input>
        </form>
        </>
    )
}