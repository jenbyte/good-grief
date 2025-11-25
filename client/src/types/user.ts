// Includes User and Partner

export enum UserType {
  ADMIN = "ADMIN",
  PARTNER = "PARTNER",
  CUSTOMER = "CUSTOMER",
}

export interface User {
  id: number;
  name: string;
  email: string;
  user_type: UserType;
  created_at: string;
  updated_at: string;
}
