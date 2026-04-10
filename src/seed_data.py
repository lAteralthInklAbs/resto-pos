"""Database seeder for menu items.

Menu items and prices extracted from original code (7.menu_interface.py, 3.cashier_pos.py):
- South Indian: Rava Dosa(70), Masala Dosa(75), Sada Dosa(60), Idli Plate(40), Vada Plate(50)
- Chinese: Chinese Bhel(25), Manchurian Soup(50), Singapore Soup(75)
- Chicken: Chicken 65(120), Chicken Crispy(135), Chicken Manchurian(130)
- Rice & Noodles: All fried rice/noodles items
"""

from src.models import MenuItem, db

MENU_ITEMS = [
    # South Indian
    {"name": "Rava Dosa", "category": "South Indian", "price": 70},
    {"name": "Masala Dosa", "category": "South Indian", "price": 75},
    {"name": "Sada Dosa", "category": "South Indian", "price": 60},
    {"name": "Idli Plate", "category": "South Indian", "price": 40},
    {"name": "Vada Plate", "category": "South Indian", "price": 50},
    # Chinese
    {"name": "Chinese Bhel", "category": "Chinese", "price": 25},
    {"name": "Manchurian Soup", "category": "Chinese", "price": 50},
    {"name": "Singapore Soup", "category": "Chinese", "price": 75},
    # Chicken
    {"name": "Chicken 65", "category": "Chicken", "price": 120},
    {"name": "Chicken Crispy", "category": "Chicken", "price": 135},
    {"name": "Chicken Manchurian", "category": "Chicken", "price": 130},
    # Rice & Noodles
    {"name": "Egg Fried Rice", "category": "Rice & Noodles", "price": 85},
    {"name": "Egg Fried Noodles", "category": "Rice & Noodles", "price": 90},
    {"name": "Chicken Fried Rice", "category": "Rice & Noodles", "price": 100},
    {"name": "Chicken Fried Noodles", "category": "Rice & Noodles", "price": 110},
    {"name": "Chicken Triple Rice", "category": "Rice & Noodles", "price": 130},
    {"name": "Chicken Triple Noodles", "category": "Rice & Noodles", "price": 150},
    {"name": "Veg Triple Rice", "category": "Rice & Noodles", "price": 110},
    {"name": "Veg Triple Noodles", "category": "Rice & Noodles", "price": 124},
]


def seed_menu_items():
    """Seed menu items if table is empty.

    Only seeds if no menu items exist to prevent duplicates on restart.
    """
    if MenuItem.query.count() == 0:
        for item_data in MENU_ITEMS:
            item = MenuItem(**item_data)
            db.session.add(item)
        db.session.commit()
        print(f"Seeded {len(MENU_ITEMS)} menu items")
    else:
        print("Menu items already exist, skipping seed")
