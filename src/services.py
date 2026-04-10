"""Business logic services for RestoPoS."""

import random
import string
from datetime import datetime


def calculate_subtotal(order_items) -> int:
    """Calculate subtotal from order items.

    Args:
        order_items: List of order items with quantity and unit_price attributes.

    Returns:
        Total sum of quantity * unit_price for all items.
    """
    return sum(item.quantity * item.unit_price for item in order_items)


def calculate_tax(subtotal: int, rate: float = 0.18) -> int:
    """Calculate tax amount.

    Matches original: Totalcost * 0.18

    Args:
        subtotal: The subtotal amount in Rs.
        rate: Tax rate (default 18% = 0.18).

    Returns:
        Tax amount as integer.
    """
    return int(subtotal * rate)


def calculate_service_charge(subtotal: int, rate: float = 0.01) -> int:
    """Calculate service charge.

    Matches original: ser_charge = Totalcost * 0.01

    Args:
        subtotal: The subtotal amount in Rs.
        rate: Service charge rate (default 1% = 0.01).

    Returns:
        Service charge amount as integer.
    """
    return int(subtotal * rate)


def calculate_total(subtotal: int, tax: int, service_charge: int) -> int:
    """Calculate grand total.

    Args:
        subtotal: Order subtotal.
        tax: Tax amount.
        service_charge: Service charge amount.

    Returns:
        Grand total.
    """
    return subtotal + tax + service_charge


def generate_reference_id() -> str:
    """Generate a reference ID matching original format.

    Original format (from 1.Customer-infopage.py lines 111-112):
    - 6 random uppercase letters
    - Customer name uppercase
    - 2 random chars from customer name

    Simplified version: 6 letters + 4 alphanumeric + 2 chars

    Returns:
        Unique reference ID string.
    """
    letters = string.ascii_uppercase
    digits = string.digits
    part1 = "".join(random.choice(letters) for _ in range(6))
    part2 = "".join(random.choice(letters + digits) for _ in range(4))
    part3 = "".join(random.choice(letters + digits) for _ in range(2))
    return f"{part1}{part2}{part3}"


def generate_receipt_number() -> str:
    """Generate a unique receipt number.

    Returns:
        Unique receipt number string.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    suffix = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    return f"RCP-{timestamp}-{suffix}"


def create_order_with_items(
    db, order_model, order_item_model, menu_item_model, quantities: dict, customer_id=None
):
    """Create an order with items.

    Args:
        db: Database session.
        order_model: Order model class.
        order_item_model: OrderItem model class.
        menu_item_model: MenuItem model class.
        quantities: Dict mapping menu_item_id to quantity.
        customer_id: Optional customer ID.

    Returns:
        Created order.

    Raises:
        ValueError: If no items with quantity > 0.
    """
    # Filter out zero quantities
    items_to_add = {k: v for k, v in quantities.items() if v > 0}

    if not items_to_add:
        raise ValueError("Cannot create order with no items")

    # Create order
    order = order_model(customer_id=customer_id)
    db.session.add(order)

    # Add order items
    for menu_item_id, quantity in items_to_add.items():
        menu_item = menu_item_model.query.get(menu_item_id)
        if menu_item and menu_item.available:
            order_item = order_item_model(
                order=order,
                menu_item_id=menu_item_id,
                quantity=quantity,
                unit_price=menu_item.price,
            )
            db.session.add(order_item)

    db.session.commit()
    return order
