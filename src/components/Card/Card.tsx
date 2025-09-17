import React from "react";
import styles from "./Card.module.css";

type CardProps = {
  id: string;
  title: string;
  isActive?: boolean;
};

const Card: React.FC<CardProps> = ({ id, title, isActive }) => {
  return (
    <>
      {isActive && (
        <div key={id} className={`${styles.card} rounded-xl mt-4 mb-8 p-5`}>
          <h3>{title}</h3>
        </div>
      )}
    </>
  );
};

export default Card;
