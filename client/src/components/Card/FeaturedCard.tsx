import React from "react";

type CardProps = {
  id: number;
  title: string;
  description?: string | null;
  imageUrl?: string | null;
};

const FeaturedCard: React.FC<CardProps> = ({
  id,
  title,
  description,
  imageUrl,
}) => {
  return (
    <>
      <div
        key={id}
        className="card featured-card cursor-pointer h-full w-full rounded-lg max-w-[48rem]"
      >
        <div className="m-auto w-2/5 shrink-0 border-surface">
          <img
            src={
              "https://images.unsplash.com/photo-1581337204873-ef36aa186caa?q=80&w=800&auto=format&fit=crop"
            }
            alt="placeholder img"
            className="h-full w-full rounded-t-lg object-cover "
          />
        </div>

        <div className=" p-5">
          <h3>{title}</h3>
        </div>
      </div>
    </>
  );
};

export default FeaturedCard;
