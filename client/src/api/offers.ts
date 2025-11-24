const API_URL = import.meta.env.VITE_API_URL;

export async function fetchOffers() {
  const res = await fetch(`${API_URL}/offers`);
  if (!res.ok) {
    throw new Error(`Failed to fetch offers: ${res.status}, ** ${res}`);
  }
  return res.json();
}
