import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]); 
  const inputEl = useRef(null);

  useEffect(() => {
    axios.get('/api/todos')
      .then(res => {
        setTodos(res.data);
      });
  }, []);

  const addTodo = () => {
    console.log(inputEl.current.value);
  };

const todoList = todos.map(todo => <li>{todo.title}</li>)

  return (
    <div className="App">
      <input ref={inputEl} type="text" />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todoList}
      </ul>
    </div>
  );
}

export default App;
