import React from "react";
import { Link } from "react-router-dom";
import Card from "../../components/Card/Card";

type HomeProps = {};

const offers = [
  {
    id: "offers0",
    title: "25% off meal delivery",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "offers1",
    title: "Free trial grief counseling",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "offers2",
    title: "Free tea at boba shop",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "offers3",
    title: "Free Cookie at Bakery",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "offers4",
    title: "Free Cookie at Bakery",
    org: "",
    orgId: "",
    isActive: true,
  },
  {
    id: "offers5",
    title: "10% off massage",
    org: "",
    orgId: "",
    isActive: true,
  },
  { id: "offers6", title: "Free reiki", org: "", orgId: "", isActive: true },
];

const Home: React.FC<HomeProps> = ({}) => {
  console.log({ offers });
  return (
    <div className="">
      <section>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>
          <Card id="featured0" title="Feaured Meditation" isActive={true} />
        </div>
      </section>

      <section>
        <div className="flex flex-row justify-between items-center-safe">
          <h2>Care Packages</h2>
          <Link to="/care-packages" className="cursor-pointer hover:underline">
            View more
          </Link>
        </div>

        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 md:grid-cols-4 md:gap-8">
          {offers.map(
            (offer) =>
              offer.isActive && (
                <Card
                  key={offer.id}
                  id={offer.id}
                  title={offer.title}
                  isActive={offer.isActive}
                />
              )
          )}
        </div>
      </section>

      <section>
        <div className="flex flex-row justify-between items-center-safe">
          <h2>Articles</h2>
          <Link to="/articles" className="cursor-pointer hover:underline">
            View more
          </Link>
        </div>
        <div></div>
      </section>
    </div>
  );
};

export default Home;
