import React, { useState } from "react";
import Todo from "./Todo.js";
import CreateToDoForm from "./CreateTodoForm.js";

const TodoList = () => {
    const [todos, setTodos] = useState([]);

    const addTask = (task) => {
        const newTodos = [...todos, { text: task, isCompleted: false }];
        setTodos(newTodos);
    };

    const completeTodo = (index) => {
        const newTodos = [...todos];
        newTodos[index].isCompleted = !newTodos[index].isCompleted;
        setTodos(newTodos);
    };

    const removeTodo = (index) => {
        const newTodos = [...todos];
        newTodos.splice(index, 1);
        setTodos(newTodos);
    };

    return (
        <div className="todo-list">
            <CreateToDoForm addTask={addTask} />
            {todos.map((todo, index) => (
                <Todo
                    key={index}
                    index={index}
                    todo={todo}
                    completeTodo={completeTodo}
                    removeTodo={removeTodo}
                />
            ))}
        </div>
    );
};

export default TodoList;
