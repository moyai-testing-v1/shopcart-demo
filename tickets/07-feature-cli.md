# [Feature] Command-line receipt printer

**Labels:** enhancement

Add `python -m shopcart receipt cart.json` that reads a JSON file of items
(`[{"sku":..., "name":..., "unit_price":..., "quantity":...}]`) plus an optional
`--coupon CODE:PERCENT:YYYY-MM-DD`, and prints a formatted receipt with a total.

**Acceptance criteria**
- Clear error message (non-zero exit) for a missing or invalid file.
- A test runs the CLI on a sample file.
- README documents the command.
