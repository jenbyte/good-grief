import React from "react";
import Card from "../Card/Card";

type Offer = {
  title: string;
  isActive: boolean;
};

type OfferListProps = {
  offers: Offer[];
};

const Base: React.FC<OfferListProps> = ({ offers }) => {
  console.log("offers", offers);

  return (
    <div className="">
      <div>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>{/* <Card /> */}</div>
      </div>

      <div>
        <h2>Offers</h2>
        <div>{/* <Card /> */}</div>
      </div>
    </div>
  );
};

export default Base;
