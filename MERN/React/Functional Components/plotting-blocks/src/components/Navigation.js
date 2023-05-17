import React from "react";
import styles from "./css/Navigation.module.css";

const Navigation = (props) => {
    return <div className={styles.div}>{props.children}</div>;
};

export default Navigation;
