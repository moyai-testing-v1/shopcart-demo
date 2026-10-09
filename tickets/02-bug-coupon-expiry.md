# [Bug] Coupons stop working on their expiry date

**Labels:** bug

A coupon with `expires_on=2026-10-31` is rejected on 31 October. Customers
expect it to work through the end of the expiry day.

**Acceptance criteria**
- `is_valid(today=expires_on)` returns `True`.
- `is_valid(today=expires_on + 1 day)` returns `False`.
- Tests cover the boundary.
