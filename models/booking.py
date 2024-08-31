from models.base import BaseModel
from typing import List
from enum import Enum

from models.seat import SeatStatus, Seat
from models.show import Show
from models.user import User


class BookingStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"


class Booking(BaseModel):
    def __init__(self, user: User, show: Show, selected_seats: List[Seat]):
        super().__init__()
        self.user = user
        self.show = show
        self.selected_seats = selected_seats
        self.status = BookingStatus.PENDING
        self.total_price = sum(seat.price for seat in selected_seats)

    def confirm_booking(self):
        self.status = BookingStatus.CONFIRMED
        for seat in self.selected_seats:
            seat.status = SeatStatus.BOOKED

    def cancel_booking(self):
        self.status = BookingStatus.CANCELLED
        for seat in self.selected_seats:
            seat.status = SeatStatus.AVAILABLE

    def __str__(self) -> str:
        return f"Booking(user={self.user.username}, show={self.show.movie.title}, seats={len(self.selected_seats)}, status={self.status})"
