from shopcart import Cart


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
