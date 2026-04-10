"""Tests for business logic services."""

import pytest

from src.services import (
    calculate_service_charge,
    calculate_subtotal,
    calculate_tax,
    calculate_total,
    generate_reference_id,
)


class MockOrderItem:
    """Mock order item for testing."""

    def __init__(self, quantity, unit_price):
        self.quantity = quantity
        self.unit_price = unit_price


class TestCalculateSubtotal:
    """Tests for subtotal calculation."""

    def test_calculate_subtotal(self):
        """Test subtotal calculation with known items."""
        items = [
            MockOrderItem(2, 70),  # 2 x Rava Dosa = 140
            MockOrderItem(1, 120),  # 1 x Chicken 65 = 120
            MockOrderItem(3, 50),  # 3 x Vada Plate = 150
        ]
        result = calculate_subtotal(items)
        assert result == 410

    def test_calculate_subtotal_single_item(self):
        """Test subtotal with single item."""
        items = [MockOrderItem(5, 75)]  # 5 x Masala Dosa
        assert calculate_subtotal(items) == 375

    def test_calculate_subtotal_empty(self):
        """Test subtotal with no items."""
        assert calculate_subtotal([]) == 0


class TestCalculateTax:
    """Tests for tax calculation."""

    def test_calculate_tax_default_rate(self):
        """Test tax at default 18% rate."""
        # 1000 * 0.18 = 180
        assert calculate_tax(1000) == 180

    def test_calculate_tax_custom_rate(self):
        """Test tax with custom rate."""
        # 1000 * 0.05 = 50
        assert calculate_tax(1000, rate=0.05) == 50

    def test_calculate_tax_zero(self):
        """Test tax on zero subtotal."""
        assert calculate_tax(0) == 0


class TestCalculateServiceCharge:
    """Tests for service charge calculation."""

    def test_calculate_service_charge_default_rate(self):
        """Test service charge at default 1% rate."""
        # 1000 * 0.01 = 10
        assert calculate_service_charge(1000) == 10

    def test_calculate_service_charge_custom_rate(self):
        """Test service charge with custom rate."""
        # 1000 * 0.02 = 20
        assert calculate_service_charge(1000, rate=0.02) == 20


class TestCalculateTotal:
    """Tests for grand total calculation."""

    def test_calculate_total(self):
        """Test total = subtotal + tax + service charge."""
        subtotal = 1000
        tax = 180  # 18%
        service = 10  # 1%
        assert calculate_total(subtotal, tax, service) == 1190

    def test_calculate_total_zero(self):
        """Test total with all zeros."""
        assert calculate_total(0, 0, 0) == 0


class TestGenerateReferenceId:
    """Tests for reference ID generation."""

    def test_generate_reference_id_returns_string(self):
        """Test that reference ID is a string."""
        ref_id = generate_reference_id()
        assert isinstance(ref_id, str)

    def test_generate_reference_id_length(self):
        """Test reference ID length is > 6 chars."""
        ref_id = generate_reference_id()
        assert len(ref_id) > 6

    def test_generate_reference_id_unique(self):
        """Test that generated IDs are unique."""
        ids = [generate_reference_id() for _ in range(100)]
        assert len(set(ids)) == 100  # All unique

    def test_generate_reference_id_format(self):
        """Test reference ID format (uppercase alphanumeric)."""
        ref_id = generate_reference_id()
        assert ref_id.isalnum()
        assert ref_id == ref_id.upper()


class TestEmptyOrderValidation:
    """Tests for empty order validation."""

    def test_empty_order_raises(self):
        """Test that creating order with no items raises ValueError."""
        from unittest.mock import MagicMock

        from src.services import create_order_with_items

        mock_db = MagicMock()
        mock_order_model = MagicMock()
        mock_order_item_model = MagicMock()
        mock_menu_item_model = MagicMock()

        with pytest.raises(ValueError, match="Cannot create order with no items"):
            create_order_with_items(
                mock_db,
                mock_order_model,
                mock_order_item_model,
                mock_menu_item_model,
                {},  # Empty quantities
            )

    def test_zero_quantities_raises(self):
        """Test that all-zero quantities raises ValueError."""
        from unittest.mock import MagicMock

        from src.services import create_order_with_items

        mock_db = MagicMock()

        with pytest.raises(ValueError):
            create_order_with_items(
                mock_db,
                MagicMock(),
                MagicMock(),
                MagicMock(),
                {1: 0, 2: 0, 3: 0},  # All zero quantities
            )
