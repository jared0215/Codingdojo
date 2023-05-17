import React from "react";
import styles from "./css/Header.module.css";

const Header = (props) => {
    return <div className={styles.div}>{props.children}</div>;
};

export default Header;
