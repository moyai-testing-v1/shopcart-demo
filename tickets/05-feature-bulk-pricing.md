# [Feature] Bulk pricing: 10% off an item when buying 5 or more

**Labels:** enhancement

Add bulk pricing: if a line item's quantity is 5 or more, that line gets 10% off
its unit price. Coupon discounts apply after bulk pricing.

**Acceptance criteria**
- Threshold and percentage are configurable constants.
- `subtotal()` reflects bulk pricing.
- Tests cover quantity 4 (no discount) and 5 (discount).
