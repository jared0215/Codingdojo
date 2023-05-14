import React, { useState } from "react";

const BoxGen = () => {
    const [inputColor, setInputColor] = useState("");
    const [boxWidth, setBoxWidth] = useState(0);
    const [boxHeight, setBoxHeight] = useState(0);
    const [boxStyleList, setBoxStyleList] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const setStyle = {
            display: "inline-block",
            margin: "10px",
            backgroundColor: inputColor,
            width: `${boxWidth}px`,
            height: `${boxHeight}px`,
        };
        setBoxStyleList([...boxStyleList, setStyle]);
        setInputColor("");
        setBoxHeight(0);
        setBoxWidth(0);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                {/* Box Color */}
                <label>Color:</label>
                <input
                    onChange={(e) => setInputColor(e.target.value)}
                    value={inputColor}
                ></input>
                {/* Box Width */}
                <label>Box Width:</label>
                <input
                    onChange={(e) => setBoxWidth(e.target.value)}
                    value={boxWidth}
                ></input>
                {/* Box Height */}
                <label>Box Height:</label>
                <input
                    onChange={(e) => setBoxHeight(e.target.value)}
                    value={boxHeight}
                ></input>
                {/* Submit Button */}
                <button type="submit">Submit</button>
            </form>
            <div>
                {boxStyleList.map((box, index) => (
                    <div key={index} style={box}>
                        <p> </p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default BoxGen;
