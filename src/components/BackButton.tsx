import { useNavigate } from "react-router-dom";

const BackButton = () => {
  const navigate = useNavigate();

  const handleGoBack = () => navigate(-1);

  return (
    <div className="back-button stroke-2">
      <button onClick={handleGoBack} className="">
        {"<"} Back
      </button>
    </div>
  );
};

export default BackButton;
