import React from "react";
import styles from "./css/Main.module.css";

const Main = (props) => {
    return <div className={styles.div}>{props.children}</div>;
};

export default Main;
