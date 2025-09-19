import React from "react";
import viteLogo from "/vite.svg";

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
        <div key={id} className="card rounded-xl p-5">
          <img src={viteLogo} className="logo mx-auto" alt="placeholder img" />
          <h3>{title}</h3>
        </div>
      )}
    </>
  );
};

export default Card;
