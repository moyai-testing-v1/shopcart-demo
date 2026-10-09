from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass, field
from .coupons import Coupon

TAX_RATE = Decimal('0.18')  # 18% GST


@dataclass
class Item:
    sku: str
    name: str
    unit_price: Decimal
    quantity: int = 1


@dataclass
class Cart:
    items: dict[str, Item] = field(default_factory=dict)
    coupon: Coupon | None = None

    def add_item(self, sku: str, name: str, unit_price: float, quantity: int = 1) -> None:
        if unit_price < 0:
            raise ValueError("unit_price must be >= 0")
        unit_price_decimal = Decimal(str(unit_price)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        if sku in self.items:
            self.items[sku].quantity += quantity
        else:
            self.items[sku] = Item(sku, name, unit_price_decimal, quantity)

    def remove_item(self, sku: str, quantity: int = 1) -> None:
        if sku not in self.items:
            raise KeyError(sku)
        self.items[sku].quantity -= quantity

    def apply_coupon(self, coupon: Coupon) -> None:
        if not coupon.is_valid():
            raise ValueError("coupon expired")
        self.coupon = coupon

    def subtotal(self) -> Decimal:
        total = sum(i.unit_price * i.quantity for i in self.items.values())
        return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def discount(self) -> Decimal:
        if not self.coupon:
            return Decimal('0.00')
        percent_off = Decimal(str(self.coupon.percent_off)) / 100
        discount_value = self.subtotal() * percent_off
        return discount_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def tax(self) -> Decimal:
        discounted_amount = self.subtotal() - self.discount()
        tax_value = discounted_amount * TAX_RATE
        return tax_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def total(self) -> Decimal:
        total_value = self.subtotal() - self.discount() + self.tax()
        return total_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def item_count(self) -> int:
        return sum(i.quantity for i in self.items.values())
