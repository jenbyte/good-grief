import React from "react";
import styles from "./Card.module.css";

type CardProps = {
  id: string;
  title: string;
  org?: string;
  orgId?: string;
  isActive?: boolean;
};

const Card: React.FC<CardProps> = ({ id, title, isActive }) => {
  return (
    <>
      {isActive && (
        <div key={id} className={`${styles.card} rounded-xl my-5 p-5`}>
          <img></img>
          <h3>{title}</h3>
        </div>
      )}
    </>
  );
};

export default Card;
