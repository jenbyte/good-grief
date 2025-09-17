import { useNavigate } from "react-router-dom";

const BackButton = () => {
  const navigate = useNavigate();

  const handleGoBack = () => navigate(-1);

  return (
    <div className="back-button">
      <button onClick={handleGoBack} className="">
        {"<"} Back
      </button>
    </div>
  );
};

export default BackButton;
