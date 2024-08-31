from models.base import BaseModel
from datetime import datetime

from models.movie import Movie
from models.screen import Screen


class Show(BaseModel):
    def __init__(
        self, movie: Movie, screen: Screen, start_time: datetime, end_time: datetime
    ):
        super().__init__()
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.end_time = end_time
        self.seats = []

    def __str__(self) -> str:
        return f"Show(movie={self.movie.title}, screen={self.screen.screen_number}, start_time={self.start_time}, end_time={self.end_time})"
