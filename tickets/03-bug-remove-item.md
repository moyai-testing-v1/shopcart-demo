# [Bug] Removing items can leave zero or negative quantities

**Labels:** bug

`remove_item("A1", 5)` on an item with quantity 2 leaves quantity `-3`, which
makes the subtotal negative. Removing exactly the remaining quantity leaves an
item with quantity 0 in the cart.

**Expected**
- When quantity reaches 0, the item is removed from the cart.
- Removing more than is in the cart raises `ValueError`, without changing the cart.
- `quantity` must be a positive integer.
