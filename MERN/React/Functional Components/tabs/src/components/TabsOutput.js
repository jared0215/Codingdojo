import React from "react";
import styles from "./css/TabsOutput.module.css";

const OutputBox = ({ content }) => {
    return <div className={styles.output}>{content}</div>;
};

export default OutputBox;
