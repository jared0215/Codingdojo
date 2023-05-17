import React, { useState } from "react";
import styles from "./css/TabsArray.module.css";
import OutputBox from "./TabsOutput.js";

const Tabs = ({ tabs = [] }) => {
    const [activeTab, setActiveTab] = useState(0);

    const contents = [
        "Content for Tab 1",
        "Content for Tab 2",
        "Content for Tab 3",
    ];

    return (
        <div className={styles.main}>
            <div className={styles.container}>
                {tabs.map((tab, index) => (
                    <button
                        key={index}
                        onClick={() => setActiveTab(index)}
                        className={
                            activeTab === index
                                ? styles.active
                                : styles.disabled
                        }
                    >
                        {tab}
                    </button>
                ))}
            </div>
            <OutputBox content={contents[activeTab]} />
        </div>
    );
};

export default Tabs;
