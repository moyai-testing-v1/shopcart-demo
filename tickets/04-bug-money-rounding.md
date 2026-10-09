# [Bug] Totals show floating-point noise (e.g. 0.30000000000000004)

**Labels:** bug

Prices use floats, so `cart.subtotal()` and `cart.total()` can return values like
`0.30000000000000004` (try 3 items at ₹0.10). Money values should be exact to 2 decimal places.

**Expected:** `subtotal()`, `discount()`, `tax()` and `total()` return values
rounded to 2 decimals (consider `decimal.Decimal`), and tax is calculated on the
discounted amount.
