from models.base import BaseModel


class Movie(BaseModel):
    def __init__(self, title: str, description: str, duration: int, ratings: float):
        super().__init__()
        self.title = title
        self.description = description
        self.duration = duration
        self.ratings = ratings

    def __str__(self) -> str:
        return f"Movie(title={self.title}, description={self.description}, duration={self.duration}, ratings={self.ratings})"
