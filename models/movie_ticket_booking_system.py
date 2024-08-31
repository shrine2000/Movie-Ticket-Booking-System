from typing import List

from models.booking import Booking
from models.movie import Movie
from models.seat import Seat
from models.show import Show
from models.theater import Theater
from models.user import User


class MovieTicketBookingSystem:
    def __init__(self):
        self.theaters = []
        self.movies = []

    def add_theater(self, theater: Theater):
        self.theaters.append(theater)

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def get_available_shows(self, movie: Movie, theater: Theater):
        available_shows = [show for show in theater.shows if show.movie == movie]
        return available_shows

    def book_ticket(self, user: User, show: Show, seats: List[Seat]):
        booking = Booking(user, show, seats)
        booking.confirm_booking()
        return booking

    def cancel_ticket(self, booking: Booking):
        booking.cancel_booking()

    def __str__(self):
        return f"MovieTicketBookingSystem(theaters={len(self.theaters)}, movies={len(self.movies)})"
