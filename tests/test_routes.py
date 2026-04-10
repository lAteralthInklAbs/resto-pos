"""Tests for Flask routes."""


class TestLoginRoutes:
    """Tests for login functionality."""

    def test_login_page_loads(self, client):
        """Test GET /login returns 200."""
        response = client.get("/login")
        assert response.status_code == 200
        assert b"Login" in response.data

    def test_login_success(self, client):
        """Test POST /login with admin/admin redirects to dashboard."""
        response = client.post(
            "/login", data={"username": "admin", "password": "admin"}, follow_redirects=False
        )
        assert response.status_code == 302
        assert "/dashboard" in response.location or "/" in response.location

    def test_login_fail(self, client):
        """Test POST /login with wrong credentials shows error."""
        response = client.post(
            "/login", data={"username": "wrong", "password": "wrong"}, follow_redirects=True
        )
        assert response.status_code == 200
        assert b"Invalid credentials" in response.data


class TestDashboardRoutes:
    """Tests for dashboard functionality."""

    def test_dashboard_requires_auth(self, client):
        """Test GET /dashboard without login redirects to login."""
        response = client.get("/dashboard", follow_redirects=False)
        assert response.status_code == 302
        assert "/login" in response.location

    def test_dashboard_with_auth(self, client):
        """Test GET /dashboard with login succeeds."""
        # Login first
        client.post("/login", data={"username": "admin", "password": "admin"})
        response = client.get("/dashboard")
        assert response.status_code == 200
        assert b"Welcome" in response.data


class TestOrderRoutes:
    """Tests for order functionality."""

    def test_order_page_shows_menu(self, app, client, seeded_db):
        """Test GET /orders/new shows menu items."""
        with app.app_context():
            # Login first
            client.post("/login", data={"username": "admin", "password": "admin"})
            response = client.get("/orders/new")
            assert response.status_code == 200
            assert b"Masala Dosa" in response.data
            assert b"Rava Dosa" in response.data

    def test_create_order(self, app, client, seeded_db):
        """Test POST /orders creates order and redirects to payment."""
        with app.app_context():
            from src.models import MenuItem

            menu_item = MenuItem.query.first()

            # Login first
            client.post("/login", data={"username": "admin", "password": "admin"})

            response = client.post(
                "/orders/new", data={f"qty_{menu_item.id}": "2"}, follow_redirects=False
            )

            assert response.status_code == 302
            assert "/payment" in response.location


class TestPaymentRoutes:
    """Tests for payment functionality."""

    def test_payment_page(self, app, client, seeded_db):
        """Test payment page shows order details."""
        with app.app_context():
            from src.models import MenuItem, Order, OrderItem, db

            # Create order
            menu_item = MenuItem.query.first()
            order = Order()
            db.session.add(order)
            order_item = OrderItem(
                order=order, menu_item_id=menu_item.id, quantity=1, unit_price=menu_item.price
            )
            db.session.add(order_item)
            db.session.commit()

            # Login
            client.post("/login", data={"username": "admin", "password": "admin"})

            response = client.get(f"/orders/{order.id}/payment")
            assert response.status_code == 200
            assert b"Payment" in response.data

    def test_process_payment(self, app, client, seeded_db):
        """Test POST /orders/<id>/pay processes payment."""
        with app.app_context():
            from src.models import MenuItem, Order, OrderItem, db

            # Create order
            menu_item = MenuItem.query.first()
            order = Order()
            db.session.add(order)
            order_item = OrderItem(
                order=order, menu_item_id=menu_item.id, quantity=1, unit_price=menu_item.price
            )
            db.session.add(order_item)
            db.session.commit()
            order_id = order.id

            # Login
            client.post("/login", data={"username": "admin", "password": "admin"})

            response = client.post(
                f"/orders/{order_id}/payment",
                data={"payment_method": "cash"},
                follow_redirects=False,
            )

            assert response.status_code == 302
            assert "/receipt" in response.location


class TestReceiptRoutes:
    """Tests for receipt functionality."""

    def test_receipt_page(self, app, client, seeded_db):
        """Test receipt page shows receipt details."""
        with app.app_context():
            from src.models import MenuItem, Order, OrderItem, Payment, db

            # Create order with payment
            menu_item = MenuItem.query.first()
            order = Order(status="paid")
            db.session.add(order)
            db.session.commit()  # Commit to get order.id

            order_item = OrderItem(
                order_id=order.id,
                menu_item_id=menu_item.id,
                quantity=1,
                unit_price=menu_item.price,
            )
            db.session.add(order_item)

            payment = Payment(
                order_id=order.id,
                subtotal=menu_item.price,
                tax_amount=int(menu_item.price * 0.18),
                service_charge=int(menu_item.price * 0.01),
                total=int(menu_item.price * 1.19),
                payment_method="cash",
            )
            db.session.add(payment)
            db.session.commit()

            # Login
            client.post("/login", data={"username": "admin", "password": "admin"})

            response = client.get(f"/orders/{order.id}/receipt")
            assert response.status_code == 200
            assert b"Receipt" in response.data or b"RCP-" in response.data


class TestOrdersListRoutes:
    """Tests for orders list functionality."""

    def test_orders_list_empty(self, client):
        """Test GET /orders with no orders shows empty state."""
        # Login first
        client.post("/login", data={"username": "admin", "password": "admin"})
        response = client.get("/orders")
        assert response.status_code == 200
        assert b"No orders yet" in response.data

    def test_orders_list_with_data(self, app, client, seeded_db):
        """Test GET /orders shows orders in table."""
        with app.app_context():
            from src.models import MenuItem, Order, OrderItem, db

            # Create an order
            menu_item = MenuItem.query.first()
            order = Order()
            db.session.add(order)
            db.session.commit()

            order_item = OrderItem(
                order_id=order.id,
                menu_item_id=menu_item.id,
                quantity=2,
                unit_price=menu_item.price,
            )
            db.session.add(order_item)
            db.session.commit()

            # Login
            client.post("/login", data={"username": "admin", "password": "admin"})

            response = client.get("/orders")
            assert response.status_code == 200
            assert b"Order History" in response.data
            assert b"ORD-" in response.data
            assert b"Pending" in response.data


class TestAPIRoutes:
    """Tests for API endpoints."""

    def test_api_menu(self, app, client, seeded_db):
        """Test /api/menu returns JSON menu items."""
        with app.app_context():
            response = client.get("/api/menu")
            assert response.status_code == 200
            data = response.get_json()
            assert len(data) == 19  # 19 menu items from seed
            assert any(item["name"] == "Masala Dosa" for item in data)
