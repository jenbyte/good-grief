// HOOKS: React state + loading + error + caching logic

import { useEffect, useState } from "react";
import { fetchOffers } from "../api/offers";
import type { Offer } from "../types/offer";

export function useOffers() {
  const [offers, setOffers] = useState<Offer[]>([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchOffers()
      .then(setOffers)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { offers, loading, error };
}
