# Initial mock data

from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.models.models import User, Offer

def mock_data(session: Session):
    user1 = User(id=1, user_type="PARTNER", name="TheZenZone", email="th3z3nzon3@email.com")
    user2 = User(id=2, user_type="PARTNER", name="Meals on Wheels", email="mealsonwheels@eats.org")
    user3 = User(id=3, user_type="PARTNER", name="Bobalicious", email="bobalicious@email.com")
    user4 = User(id=4, user_type="PARTNER", name="BAKED", email="baked@email.org")
    user5 = User(id=5, user_type="PARTNER", name="Therapists United", email="therapists.united@gov.ca")
    user6 = User(id=6, user_type="ADMIN", name="Glenda Jenga", email="GlendaJ@gmail.com")

    offer1 = Offer(id=1, title="25% off meal delivery", partner_id=2)
    offer2 = Offer(id=2, title="Free trial grief counseling", partner_id=5)
    offer3 = Offer(id=3, title="Free tea at boba shop", partner_id=3)
    offer4 = Offer(id=4, title="Free Cookie at Bakery", partner_id=3)
    offer5 = Offer(id=5, title="Complimentary Cookie at BAKED", partner_id=4)
    offer6 = Offer(id=6, title="10% off massage", partner_id=5)
    offer7 = Offer(id=7, title="Free reiki", partner_id=1)
    offer8 = Offer(id=8, title="First 3 months free food delivery", partner_id=2)
    offer9 = Offer(id=9, title="20% Off Groceries", partner_id=2)
    
    session.add_all([
        user1, user2, user3, user4, user5, user6, offer1, offer2, offer3, offer4, offer5, offer6, offer7, offer8, offer9
    ])
    
    session.commit()
    
