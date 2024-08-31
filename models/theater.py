from models.base import BaseModel


class Theater(BaseModel):
    def __init__(self, name: str, location: str):
        super().__init__()
        self.name = name
        self.location = location
        self.screens = []
        self.shows = []

    def __str__(self) -> str:
        return f"Theater(name={self.name}, location={self.location}, screens={len(self.screens)}, shows={len(self.shows)})"
