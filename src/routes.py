"""Flask routes for RestoPoS."""

from functools import wraps

from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for

from src.models import Customer, MenuItem, Order, OrderItem, Payment, db
from src.services import (
    calculate_service_charge,
    calculate_tax,
    calculate_total,
)

bp = Blueprint("main", __name__)


def login_required(f):
    """Decorator to require login for routes."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(url_for("main.login"))
        return f(*args, **kwargs)

    return decorated_function


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Cashier login page."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Demo credentials: admin/admin
        if username == "admin" and password == "admin":
            session["logged_in"] = True
            session["username"] = username
            flash("Welcome, Cashier!", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Invalid credentials. Try admin/admin for demo.", "error")

    return render_template("login.html")


@bp.route("/logout")
def logout():
    """Clear session and redirect to login."""
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("main.login"))


@bp.route("/")
@bp.route("/dashboard")
@login_required
def dashboard():
    """Main dashboard."""
    return render_template("dashboard.html")


@bp.route("/customers/new", methods=["GET", "POST"])
@login_required
def new_customer():
    """Customer registration form."""
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")

        if not name:
            flash("Customer name is required.", "error")
            return render_template("customer_form.html")

        customer = Customer(name=name.upper(), phone=phone, address=address)
        db.session.add(customer)
        db.session.commit()

        flash(f"Customer registered! Reference ID: {customer.reference_id}", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("customer_form.html")


@bp.route("/orders/new", methods=["GET", "POST"])
@login_required
def new_order():
    """Order entry page."""
    menu_items = MenuItem.query.filter_by(available=True).all()

    # Group by category
    categories = {}
    for item in menu_items:
        if item.category not in categories:
            categories[item.category] = []
        categories[item.category].append(item)

    if request.method == "POST":
        # Parse quantities from form
        quantities = {}
        for item in menu_items:
            qty = request.form.get(f"qty_{item.id}", 0, type=int)
            if qty > 0:
                quantities[item.id] = qty

        if not quantities:
            flash("Please select at least one item.", "error")
            return render_template("order.html", categories=categories)

        # Create order
        order = Order()
        db.session.add(order)

        for menu_item_id, quantity in quantities.items():
            menu_item = MenuItem.query.get(menu_item_id)
            order_item = OrderItem(
                order=order,
                menu_item_id=menu_item_id,
                quantity=quantity,
                unit_price=menu_item.price,
            )
            db.session.add(order_item)

        db.session.commit()
        return redirect(url_for("main.payment", order_id=order.id))

    return render_template("order.html", categories=categories)


@bp.route("/orders/<int:order_id>/payment", methods=["GET", "POST"])
@login_required
def payment(order_id):
    """Payment page."""
    order = Order.query.get_or_404(order_id)

    if order.status == "paid":
        return redirect(url_for("main.receipt", order_id=order.id))

    subtotal = order.subtotal
    tax = calculate_tax(subtotal)
    service_charge = calculate_service_charge(subtotal)
    total = calculate_total(subtotal, tax, service_charge)

    if request.method == "POST":
        payment_method = request.form.get("payment_method", "cash")

        payment_record = Payment(
            order_id=order.id,
            subtotal=subtotal,
            tax_amount=tax,
            service_charge=service_charge,
            total=total,
            payment_method=payment_method,
        )
        db.session.add(payment_record)

        order.status = "paid"
        db.session.commit()

        flash("Payment successful!", "success")
        return redirect(url_for("main.receipt", order_id=order.id))

    return render_template(
        "payment.html",
        order=order,
        subtotal=subtotal,
        tax=tax,
        service_charge=service_charge,
        total=total,
    )


@bp.route("/orders/<int:order_id>/receipt")
@login_required
def receipt(order_id):
    """Receipt page."""
    order = Order.query.get_or_404(order_id)
    payment_record = order.payment

    if not payment_record:
        flash("Payment not found for this order.", "error")
        return redirect(url_for("main.dashboard"))

    return render_template("receipt.html", order=order, payment=payment_record)


@bp.route("/api/menu")
def api_menu():
    """JSON API for menu items."""
    menu_items = MenuItem.query.filter_by(available=True).all()
    return jsonify([item.to_dict() for item in menu_items])
