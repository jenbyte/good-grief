import React from "react";
import { Link } from "react-router-dom";
import { useOffers } from "../../hooks/useOffers";
import Card from "../../components/Card/Card";
import FeaturedCard from "../../components/Card/FeaturedCard";

type HomeProps = {};

const Home: React.FC<HomeProps> = ({}) => {
  const { offers, loading, error } = useOffers();

  console.log("offers: ", offers);
  return (
    <div className="home-page">
      <section>
        <div className=""></div>
        <h1>Hi, how are you feeling today?</h1>

        <div>
          <FeaturedCard id={0} title="Feaured Meditation" />
        </div>
      </section>

      <section>
        <div className="flex flex-row justify-between items-center-safe">
          <h2>Care Packages</h2>
          <Link to="/care-packages" className="cursor-pointer hover:underline">
            View more
          </Link>
        </div>

        {/* <div className="overflow-x-scroll min-h-[140px] w-full grid grid-cols-1 gap-5 sm:grid-cols-2 md:grid-cols-4 md:gap-8"> */}
        <div className="flex overflow-x-scroll min-h-[140px] gap-5 md:gap-8">
          {offers.map((offer) => {
            return (
              <Card
                key={offer.id}
                id={offer.id}
                title={offer.title}
                description={offer.description}
                // imageUrl={offer.image_url}
                imageUrl={
                  "https://images.unsplash.com/photo-1581337204873-ef36aa186caa?q=80&w=800&auto=format&fit=crop"
                }
                isActive={offer.is_active}
              />
            );
          })}
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
