import React from "react";

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
        <div key={id} className="card rounded-xl my-5 p-5">
          <img></img>
          <h3>{title}</h3>
        </div>
      )}
    </>
  );
};

export default Card;
