import React, { useState } from "react";

const Todo = ({ todo, index, completeTodo, removeTodo }) => {
    const [text, setText] = useState(todo.text);
    const [completed, setCompleted] = useState(todo.completed);

    const createTodo = (e) => {
        e.preventDefault();
        const newTodo = {
            text,
            completed,
        };
        completeTodo(index, newTodo);
        setText("");
        setCompleted(false);
    };

    return (
        <div className="todo">
            <form onSubmit={createTodo}>
                <div className="form-group">
                    <label htmlFor="text">Text</label>
                    <input
                        type="text"
                        name="text"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                    />
                    <button type="submit" className="btn btn-primary">
                        Add
                    </button>
                </div>
            </form>
            <div className="todo-actions">
                <p>`${newTodo}`</p>
                <button
                    type="button"
                    className="btn btn-danger"
                    onClick={() => removeTodo(index)}
                >
                    Delete
                </button>
            </div>
        </div>
    );
};

export default Todo;
