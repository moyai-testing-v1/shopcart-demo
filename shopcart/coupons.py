from dataclasses import dataclass
from datetime import date


@dataclass
class Coupon:
    code: str
    percent_off: float  # e.g. 10 means 10% off
    expires_on: date

    def is_valid(self, today: date | None = None) -> bool:
        today = today or date.today()
        return today < self.expires_on
