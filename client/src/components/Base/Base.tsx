import React from "react";
import Card from "../Card/Card";

type Coupon = {
  title: string;
  isActive: boolean;
};

type CouponListProps = {
  coupons: Coupon[];
};

const Base: React.FC<CouponListProps> = ({ coupons }) => {
  console.log("coupons", coupons);

  return (
    <div className="">
      <div>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>{/* <Card /> */}</div>
      </div>

      <div>
        <h2>Coupons</h2>
        <div>{/* <Card /> */}</div>
      </div>
    </div>
  );
};

export default Base;
