"""Tests for database models."""
import pytest
from src.models import MenuItem, Customer, Order, OrderItem, Payment


class TestMenuItem:
    """Tests for MenuItem model."""

    def test_create_menu_item(self, app, db_session):
        """Test creating and querying a menu item."""
        with app.app_context():
            item = MenuItem(name='Test Item', category='Test', price=100)
            db_session.session.add(item)
            db_session.session.commit()

            queried = MenuItem.query.filter_by(name='Test Item').first()
            assert queried is not None
            assert queried.price == 100
            assert queried.category == 'Test'
            assert queried.available is True

    def test_menu_item_to_dict(self, app, db_session):
        """Test MenuItem to_dict method."""
        with app.app_context():
            item = MenuItem(name='Test Item', category='Test', price=50)
            db_session.session.add(item)
            db_session.session.commit()

            data = item.to_dict()
            assert data['name'] == 'Test Item'
            assert data['price'] == 50
            assert data['available'] is True


class TestCustomer:
    """Tests for Customer model."""

    def test_create_customer(self, app, db_session):
        """Test customer creation with auto-generated reference ID."""
        with app.app_context():
            customer = Customer(name='John Doe', phone='9876543210')
            db_session.session.add(customer)
            db_session.session.commit()

            assert customer.reference_id is not None
            assert len(customer.reference_id) > 6
            assert customer.name == 'John Doe'

    def test_customer_reference_id_unique(self, app, db_session):
        """Test that customer reference IDs are unique."""
        with app.app_context():
            c1 = Customer(name='Customer 1')
            c2 = Customer(name='Customer 2')
            db_session.session.add_all([c1, c2])
            db_session.session.commit()

            assert c1.reference_id != c2.reference_id


class TestOrder:
    """Tests for Order model."""

    def test_create_order_with_items(self, app, seeded_db):
        """Test order creation with order items."""
        with app.app_context():
            menu_item = MenuItem.query.first()
            order = Order()
            seeded_db.session.add(order)

            order_item = OrderItem(
                order=order,
                menu_item_id=menu_item.id,
                quantity=3,
                unit_price=menu_item.price
            )
            seeded_db.session.add(order_item)
            seeded_db.session.commit()

            assert order.reference_id is not None
            assert len(order.items) == 1
            assert order.items[0].quantity == 3
            assert order.subtotal == 3 * menu_item.price

    def test_order_status_default(self, app, db_session):
        """Test order default status is pending."""
        with app.app_context():
            order = Order()
            db_session.session.add(order)
            db_session.session.commit()

            assert order.status == 'pending'


class TestPayment:
    """Tests for Payment model."""

    def test_create_payment(self, app, seeded_db):
        """Test payment creation with auto-generated receipt number."""
        with app.app_context():
            order = Order()
            seeded_db.session.add(order)
            seeded_db.session.commit()

            payment = Payment(
                order_id=order.id,
                subtotal=1000,
                tax_amount=180,
                service_charge=10,
                total=1190,
                payment_method='cash'
            )
            seeded_db.session.add(payment)
            seeded_db.session.commit()

            assert payment.receipt_number is not None
            assert payment.receipt_number.startswith('RCP-')
            assert payment.total == 1190

    def test_payment_receipt_unique(self, app, seeded_db):
        """Test that receipt numbers are unique."""
        with app.app_context():
            o1 = Order()
            o2 = Order()
            seeded_db.session.add_all([o1, o2])
            seeded_db.session.commit()

            p1 = Payment(order_id=o1.id, subtotal=100, tax_amount=18,
                        service_charge=1, total=119, payment_method='cash')
            p2 = Payment(order_id=o2.id, subtotal=200, tax_amount=36,
                        service_charge=2, total=238, payment_method='card')
            seeded_db.session.add_all([p1, p2])
            seeded_db.session.commit()

            assert p1.receipt_number != p2.receipt_number
