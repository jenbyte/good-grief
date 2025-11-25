// import as `type`
// e.g. import type { Offer } from "../types/offer"

export interface Offer {
  id: number;
  title: string;
  description?: string | null;
  image_url?: string | "";
  is_active: boolean;
  partner_id: number;
  date_start: string;
  date_expires: string | null;
  usage_limit: number | null;
  usage_count: number;
  created_at: string;
  updated_at: string;
}
