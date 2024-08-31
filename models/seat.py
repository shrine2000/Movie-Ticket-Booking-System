from models.base import BaseModel
from enum import Enum


class SeatType(Enum):
    NORMAL = "Normal"
    PREMIUM = "Premium"


class SeatStatus(Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"


class Seat(BaseModel):
    def __init__(self, row: int, column: int, seat_type: SeatType, price: float):
        super().__init__()
        self.row = row
        self.column = column
        self.seat_type = seat_type
        self.price = price
        self.status = SeatStatus.AVAILABLE

    def __str__(self) -> str:
        return f"Seat(row={self.row}, column={self.column}, type={self.seat_type}, price={self.price}, status={self.status})"
