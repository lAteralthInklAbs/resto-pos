"""SQLAlchemy database models for RestoPoS."""
import random
import string
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def generate_reference_id() -> str:
    """Generate a reference ID matching original format: 6 random letters + digits + 2 random chars."""
    letters = string.ascii_uppercase
    digits = string.digits
    # 6 random letters + 4 random alphanumeric + 2 random letters
    return ''.join(random.choice(letters) for _ in range(6)) + \
           ''.join(random.choice(letters + digits) for _ in range(4)) + \
           ''.join(random.choice(letters + digits) for _ in range(2))


def generate_receipt_number() -> str:
    """Generate a unique receipt number."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    return f"RCP-{timestamp}-{suffix}"


class MenuItem(db.Model):
    """Menu item model."""
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # South Indian, Chinese, Chicken, Rice & Noodles
    price = db.Column(db.Integer, nullable=False)  # Price in Rs.
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<MenuItem {self.name} Rs.{self.price}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'available': self.available
        }


class Customer(db.Model):
    """Customer model."""
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    reference_id = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, **kwargs):
        if 'reference_id' not in kwargs:
            kwargs['reference_id'] = generate_reference_id()
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Customer {self.name} ({self.reference_id})>'


class Order(db.Model):
    """Order model."""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=True)  # Nullable for walk-in
    reference_id = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, paid, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    payment = db.relationship('Payment', backref='order', uselist=False)

    def __init__(self, **kwargs):
        if 'reference_id' not in kwargs:
            kwargs['reference_id'] = generate_reference_id()
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Order {self.reference_id} ({self.status})>'

    @property
    def subtotal(self):
        """Calculate order subtotal."""
        return sum(item.subtotal for item in self.items)


class OrderItem(db.Model):
    """Order item model."""
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)  # Price at time of order

    menu_item = db.relationship('MenuItem')

    @property
    def subtotal(self):
        """Calculate line item subtotal."""
        return self.quantity * self.unit_price

    def __repr__(self):
        return f'<OrderItem {self.quantity}x {self.menu_item.name if self.menu_item else "Unknown"}>'


class Payment(db.Model):
    """Payment model."""
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)
    tax_rate = db.Column(db.Float, default=0.18)  # 18% tax
    tax_amount = db.Column(db.Integer, nullable=False)
    service_charge = db.Column(db.Integer, nullable=False)  # 1% service charge
    total = db.Column(db.Integer, nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)  # cash, card
    paid_at = db.Column(db.DateTime, default=datetime.utcnow)
    receipt_number = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, **kwargs):
        if 'receipt_number' not in kwargs:
            kwargs['receipt_number'] = generate_receipt_number()
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Payment {self.receipt_number} Rs.{self.total}>'
