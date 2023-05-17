import React from "react";
import styles from "./css/Advertisement.module.css";

const Advertisement = (props) => {
    return <div className={styles.advert}>{props.children}</div>;
};

export default Advertisement;
