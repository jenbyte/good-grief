import React from "react";
import { Link, useNavigate } from "react-router-dom";
import BackButton from "../../components/BackButton";

const Savings = () => {
  const navigate = useNavigate();

  const handleGoBack = () => navigate(-1);
  return (
    <div>
      <BackButton />
      <h1>Care Packages</h1>
    </div>
  );
};

export default Savings;
