import React, { useState } from "react";

const CreateToDoForm = (props) => {
    const [todo, setTodo] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        props.addTask(todo);
        setTodo("");
    };

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="todo">Enter a new task:</label>
            <input
                type="text"
                name="todo"
                onChange={(e) => setTodo(e.target.value)}
                value={todo}
            />
            <input type="submit" value="Add Task" />
        </form>
    );
};

export default CreateToDoForm;
