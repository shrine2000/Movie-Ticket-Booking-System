from models.base import BaseModel


class Screen(BaseModel):
    def __init__(self, screen_number: int):
        super().__init__()
        self.screen_number = screen_number
        self.shows = []

    def __str__(self) -> str:
        return f"Screen(screen_number={self.screen_number}, shows={len(self.shows)})"
