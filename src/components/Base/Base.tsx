import React from "react";
import Card from "../Card/Card";

type Saving = {
  title: string;
  isActive: boolean;
};

type SavingListProps = {
  savings: Saving[];
};

const Base: React.FC<SavingListProps> = ({ savings }) => {
  console.log("savings", savings);

  return (
    <div className="">
      <div>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>{/* <Card /> */}</div>
      </div>

      <div>
        <h2>Savings</h2>
        <div>{/* <Card /> */}</div>
      </div>
    </div>
  );
};

export default Base;
