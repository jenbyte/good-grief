import BackButton from "../../components/BackButton";
import HorizontalCard from "../../components/Card/HorizontalCard";
import { useOffers } from "../../hooks/useOffers";

const Offers = () => {
  const { offers, loading, error } = useOffers();

  console.log("OffersPage: ", offers);
  return (
    <div>
      <BackButton />
      <h1>Care Packages</h1>

      <div className="">
        {offers.map((offer) => {
          console.log("OffersPage:", offer);
          return (
            <HorizontalCard
              id={offer.id}
              title={offer.title}
              description={offer.description}
              imageUrl={offer.image_url}
              isActive={offer.is_active}
            />
          );
        })}
      </div>
    </div>
  );
};

export default Offers;
