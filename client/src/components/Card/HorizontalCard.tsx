import React from "react";

type CardProps = {
  id: number;
  title: string;
  description?: string | null;
  imageUrl?: string | "";
  isActive: boolean;
};

const HorizontalCard: React.FC<CardProps> = ({
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
          className="cursor-pointer h-full w-full max-w-[48rem] flex flex-row shadow-sm sm:mb-2 md:mb-3"
        >
          <div className="m-0 w-2/5 shrink-0 border-surface">
            <img
              // src={imageUrl}
              src={
                "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1471&q=80"
              }
              alt="card-image"
              className="h-full w-full rounded-l-md rounded-r-none object-cover"
            />
          </div>

          <div className="border-solid border-1 border-current border-l-none rounded-r-md p-5">
            <h3 className="mb-2">{title}</h3>
            {/* <p className="mb-8 text-foreground">{description}</p> */}
            <p className="mb-8 text-foreground">
              Like so many organizations these days, Autodesk is a company in
              transition. It was until recently a traditional boxed software
              company selling licenses. Yet its own business model disruption is
              only part of the story
            </p>
          </div>
        </div>
      )}
    </>
  );
};

export default HorizontalCard;
