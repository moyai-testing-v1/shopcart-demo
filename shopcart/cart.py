from dataclasses import dataclass, field

from .coupons import Coupon

TAX_RATE = 0.18  # 18% GST


@dataclass
class Item:
    sku: str
    name: str
    unit_price: float
    quantity: int = 1


@dataclass
class Cart:
    items: dict[str, Item] = field(default_factory=dict)
    coupon: Coupon | None = None

    def add_item(self, sku: str, name: str, unit_price: float, quantity: int = 1) -> None:
        if unit_price < 0:
            raise ValueError("unit_price must be >= 0")
        if sku in self.items:
            self.items[sku].quantity += quantity
        else:
            self.items[sku] = Item(sku, name, unit_price, quantity)

    def remove_item(self, sku: str, quantity: int = 1) -> None:
        if sku not in self.items:
            raise KeyError(sku)
        self.items[sku].quantity -= quantity

    def apply_coupon(self, coupon: Coupon) -> None:
        if not coupon.is_valid():
            raise ValueError("coupon expired")
        self.coupon = coupon

    def subtotal(self) -> float:
        return sum(i.unit_price * i.quantity for i in self.items.values())

    def discount(self) -> float:
        if not self.coupon:
            return 0.0
        return self.coupon.percent_off

    def tax(self) -> float:
        return (self.subtotal() - self.discount()) * TAX_RATE

    def total(self) -> float:
        return self.subtotal() - self.discount() + self.tax()

    def item_count(self) -> int:
        return sum(i.quantity for i in self.items.values())
