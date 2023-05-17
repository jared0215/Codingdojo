import React from "react";
import styles from "./css/SubContents.module.css";

const SubContents = (props) => {
    return <div className={styles.subcontent}>{props.children}</div>;
};

export default SubContents;
