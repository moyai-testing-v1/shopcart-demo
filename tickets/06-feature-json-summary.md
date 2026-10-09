# [Feature] Export a cart summary as JSON

**Labels:** enhancement

Add `Cart.to_dict()` and `Cart.to_json()` returning items (sku, name, unit_price,
quantity, line_total), coupon code (or null), subtotal, discount, tax and total.

**Acceptance criteria**
- Output is valid JSON with money values rounded to 2 decimals.
- Tests check the structure for an empty cart and a cart with a coupon.
