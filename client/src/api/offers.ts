const API_URL = import.meta.env.VITE_API_URL;

export async function fetchOffers() {
  const res = await fetch(`${API_URL}/offers`);
  if (!res.ok) {
    throw new Error(`Failed to fetch offers: ${res.status}`);
  }
  return res.json();
}

export async function createOffer() {
  const res = await fetch(`${API_URL}/offers`);
  if (!res.ok) {
    throw new Error(`Failed to create a new offer: ${res.status}`);
  }
  return res.json();
}
