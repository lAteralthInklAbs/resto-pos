"""Pytest fixtures for RestoPoS tests."""
import pytest
from app import create_app
from src.models import db, MenuItem, Customer, Order, OrderItem, Payment
from src.config import Config


class TestConfig(Config):
    """Test configuration with in-memory SQLite."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test-secret'


@pytest.fixture
def app():
    """Create test application."""
    app = create_app(TestConfig)
    yield app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def db_session(app):
    """Create database session."""
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


@pytest.fixture
def seeded_db(app, db_session):
    """Database with seeded menu items."""
    from src.seed_data import seed_menu_items
    with app.app_context():
        seed_menu_items()
        yield db_session


@pytest.fixture
def sample_customer(app, db_session):
    """Create sample customer."""
    with app.app_context():
        customer = Customer(name='TEST CUSTOMER', phone='1234567890')
        db_session.session.add(customer)
        db_session.session.commit()
        yield customer


@pytest.fixture
def sample_order(app, seeded_db, sample_customer):
    """Create sample order with items."""
    with app.app_context():
        # Re-fetch customer in this context
        customer = Customer.query.first()
        menu_item = MenuItem.query.first()

        order = Order(customer_id=customer.id)
        seeded_db.session.add(order)

        order_item = OrderItem(
            order=order,
            menu_item_id=menu_item.id,
            quantity=2,
            unit_price=menu_item.price
        )
        seeded_db.session.add(order_item)
        seeded_db.session.commit()
        yield order
