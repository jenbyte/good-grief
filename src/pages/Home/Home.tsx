import React from "react";
import Card from "../../components/Card/Card";
import Savings from "../Savings";

type HomeProps = {};

const savings = [
  {
    id: "savings0",
    title: "25% off meal delivery",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "savings1",
    title: "Free trial grief counseling",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "savings2",
    title: "Free tea at boba shop",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "savings3",
    title: "Free Cookie at Bakery",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "savings4",
    title: "20% off groceries",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "savings5",
    title: "10% off massage",
    org: "",
    orgId: "",
    isActive: true,
  },
  { id: "savings6", title: "Free reiki", org: "", orgId: "", isActive: true },
];

const Home: React.FC<HomeProps> = ({}) => {
  console.log({ savings });
  return (
    <div className="">
      <div>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>
          <Card id="featured0" title="Feaured Meditation" isActive={true} />
        </div>
      </div>

      <div>
        <h2
          className="cursor-pointer hover:underline"
          role="link"
          tabIndex={0}
          // onClick={go}
          // onKeyDown={(e) => e.key === "Enter" && go()
        >
          Savings
        </h2>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
          {savings.map(
            (saving) =>
              saving.isActive && (
                <Card
                  key={saving.id}
                  id={saving.id}
                  title={saving.title}
                  isActive={saving.isActive}
                />
              )
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
