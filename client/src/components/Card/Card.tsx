import React from "react";
import viteLogo from "/vite.svg";

type CardProps = {
  id: number;
  title: string;
  description?: string | null;
  imageUrl?: string | null;
  isActive: boolean;
};

const Card: React.FC<CardProps> = ({
  id,
  title,
  description,
  imageUrl,
  isActive,
}) => {
  console.log("Offer", title, isActive);

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
