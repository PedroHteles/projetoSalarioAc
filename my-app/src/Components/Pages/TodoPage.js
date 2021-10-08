import React from  'react';
import api from '../../services/api';
import { Form } from '../Form/form';

export const TodoPage = () =>{
    const [resultado, setResultado] = React.useState([])
    const[addTodo, setAddTodo] = React.useState('')
    const[teste, setAddTodo1] = React.useState('')

    // useEffect(() => {
    //     fetch('/teste').then(response => {
    //         if(response.ok){
    //             return response.json()
    //         }
    //     }).then(data => setTodo(data))
    // }, [])

    // const handleFormChange = (inputValue) =>{
    //     setAddTodo(inputValue)
        
    // }
    // const handleFormChange1 = (inputValue) =>{
    //     setAddTodo1(inputValue)
    // }

    const handleFormSubmit = async () => {
        console.log(addTodo,teste)
        const res = await api.post('/api/calculaSalario',{salario:addTodo,dependentes:teste})
        setResultado(res.data)
    }
    
    return(
        <>
            <Form userInput={addTodo} userInput1={teste} onFormChange={(e) => setAddTodo(e)} onFormChange1={(e) => setAddTodo1(e)} onFormSubmit={handleFormSubmit}  ></Form>
            <h1>{addTodo}</h1>
            <h1>{teste}</h1>
            <h1>Total descontato {resultado.inss}</h1>
            <h1>Salario:{resultado.salario} </h1>
        </>
    )
}