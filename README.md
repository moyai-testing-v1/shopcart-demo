# shopcart-demo

A tiny shopping-cart library with **known bugs and missing features**, made for
testing the Moyai coding agent. See `tickets/` (or the repo's GitHub Issues).

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
pytest
```

The existing tests pass, but they don't cover the bugs. Each fix should add a
test that fails before the fix and passes after it.
