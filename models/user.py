from typing import Optional

from models.base import BaseModel


class User(BaseModel):
    def __init__(self, username: str, email: str, uid: Optional[str] = None):
        super().__init__(uid=uid)
        self.username = username
        self.email = email

    def __str__(self) -> str:
        return (
            f"User(username={self.username}, email={self.email}, {super().__str__()})"
        )
