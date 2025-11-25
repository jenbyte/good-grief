import React from "react";

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
  return (
    <>
      {isActive && (
        <div
          key={id}
          className="card cursor-pointer h-full w-full max-w-[24rem] overflow-hidden rounded-md"
        >
          <div className="m-auto shrink-0">
            <img
              // src={imageUrl}
              src={
                "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1471&q=80"
              }
              alt="offer img"
              className="h-full w-full rounded-t-md object-cover"
            />
          </div>

          <div className="p-4">
            <h4>{title}</h4>
          </div>
        </div>
      )}
    </>
  );
};

export default Card;
