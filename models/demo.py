from datetime import datetime

from models.movie import Movie
from models.movie_ticket_booking_system import MovieTicketBookingSystem
from models.screen import Screen
from models.seat import SeatType, Seat
from models.show import Show
from models.theater import Theater
from models.user import User

if __name__ == "__main__":
    system = MovieTicketBookingSystem()

    movie1 = Movie(
        title="The Matrix", description="A sci-fi classic", duration=150, ratings=8.7
    )
    system.add_movie(movie1)

    theater1 = Theater(name="PVR Cinemas", location="Downtown")
    system.add_theater(theater1)

    screen1 = Screen(screen_number=1)
    theater1.screens.append(screen1)

    show1 = Show(
        movie=movie1,
        screen=screen1,
        start_time=datetime(2024, 9, 1, 14, 30),
        end_time=datetime(2024, 9, 1, 16, 30),
    )
    theater1.shows.append(show1)

    for row in range(1, 6):
        for col in range(1, 11):
            seat_type = SeatType.NORMAL if row <= 3 else SeatType.PREMIUM
            seat_price = 100 if seat_type == SeatType.NORMAL else 150
            seat = Seat(row=row, column=col, seat_type=seat_type, price=seat_price)
            show1.seats.append(seat)

    user1 = User(username="john_doe", email="john@example.com")
    selected_seats = [show1.seats[0], show1.seats[1]]
    booking1 = system.book_ticket(user=user1, show=show1, seats=selected_seats)
    print(booking1)
