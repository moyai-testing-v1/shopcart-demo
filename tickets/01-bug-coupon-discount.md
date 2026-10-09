# [Bug] Percentage coupons subtract a flat amount instead of a percentage

**Labels:** bug

A `Coupon(percent_off=10)` on a ₹500 cart should take off ₹50, but the cart only
subtracts ₹10. `Cart.discount()` returns `percent_off` directly instead of a
percentage of the subtotal.

**Expected:** discount = subtotal × percent_off / 100, and the discount can never
exceed the subtotal.

**Acceptance criteria**
- A 10% coupon on a ₹500 cart gives a ₹50 discount.
- A 150% coupon never makes the total negative.
- Tests cover both cases.
