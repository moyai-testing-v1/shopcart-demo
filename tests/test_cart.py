from shopcart import Cart
import pytest
from decimal import Decimal

def test_add_and_subtotal():
    cart = Cart()
    cart.add_item("A1", "Pen", 10.0, 2)
    cart.add_item("B2", "Notebook", 50.0)
    assert cart.subtotal() == 70.0
    assert cart.item_count() == 3

def test_adding_same_sku_merges_quantity():
    cart = Cart()
    cart.add_item("A1", "Pen", 10.0)
    cart.add_item("A1", "Pen", 10.0, 3)
    assert cart.items["A1"].quantity == 4

def test_total_without_coupon_includes_tax():
    cart = Cart()
    cart.add_item("A1", "Pen", 100.0)
    assert round(cart.total(), 2) == 118.0

# New test for floating-point noise bug
@pytest.mark.parametrize("prices, quantities, expected_subtotal", [
    ([0.1, 0.1, 0.1], [1, 1, 1], 0.30),  # Known float issue case
    ([0.1, 0.2], [1, 1], 0.20),
    ([0.15, 0.15], [1, 1], 0.30),
])
def test_subtotal_and_total_rounding(prices, quantities, expected_subtotal):
    cart = Cart()
    for p, q in zip(prices, quantities):
        cart.add_item("X", "Item", p, q)
    subtotal = cart.subtotal()
    total = cart.total()
    # We expect subtotal to equal expected as Decimal rounded to two decimals
    assert subtotal == round(Decimal(expected_subtotal), 2)
    # Total should also be consistent with tax calculated on discounted amount
    discounted_amount = subtotal - cart.discount()
    expected_total = round(discounted_amount * Decimal('1.18'), 2)
    assert round(total, 2) == expected_total
