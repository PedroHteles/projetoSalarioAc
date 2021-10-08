import React,{useState, useEffect} from  'react';
import { Card } from '../Card/card';
import { Form } from '../Form/form';

export const TodoPage = () =>{

    const [todo, setTodo] = useState([])
    const[addTodo, setAddTodo] = useState('')
    const[teste, setAddTodo1] = useState('')

    useEffect(() => {
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => setTodo(data))
    }, [])

    const handleFormChange = (inputValue) =>{
        setAddTodo(inputValue)
        console.log(addTodo)
    }

    const handleFormChange1 = (inputValue) =>{
        setAddTodo1(inputValue)
        console.log(inputValue)
    }

    const handleFormSubmit = () => {
        fetch('/api/create',{
            method:'POST',
            body: JSON.stringify({
                content:addTodo,
                teste:teste
            }),
            headers:{
                "Content-type": "application/json; charset=utf-8"
            }
        }).then(response => response.json())
          .then(message => {
              console.log(message)
              setAddTodo('')
              setAddTodo1('')
          })

    }



    const getLatestTodos = () => {
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => setAddTodo(data))
    }
    
    return(
        <>
            <Form userInput={addTodo} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit} userInput1={teste} onFormChange1={handleFormChange1}></Form>
            <Card listOfTodos= {todo}/>
        </>
    )
}