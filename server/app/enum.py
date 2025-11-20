from enum import Enum

class UserType(str, Enum):
    ADMIN = "ADMIN"
    PARTNER = "PARTNER"
    CUSTOMER = "CUSTOMER"