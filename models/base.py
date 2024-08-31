from datetime import datetime
from uuid import uuid4
from typing import Any, Optional


class BaseModel:
    def __init__(self, uid: Optional[str] = None):
        self._id = self._generate_id()
        self._uid = uid or self._generate_uid()
        self._created_at = datetime.now()
        self._last_updated_at = self._created_at
        self._deleted_at = None
        self._is_active = True
        self._version = 1

    @staticmethod
    def _generate_id() -> str:
        return str(uuid4())

    @staticmethod
    def _generate_uid() -> str:
        return str(uuid4())

    @property
    def id(self) -> str:
        return self._id

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def last_updated_at(self) -> datetime:
        return self._last_updated_at

    @property
    def deleted_at(self) -> Optional[datetime]:
        return self._deleted_at

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def version(self) -> int:
        return self._version

    @property
    def is_deleted(self) -> bool:
        return not self._is_active and self._deleted_at is not None

    def update_timestamp(self):
        self._last_updated_at = datetime.now()
        self._version += 1

    def soft_delete(self):
        self._is_active = False
        self._deleted_at = datetime.now()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uid": self.uid,
            "created_at": self.created_at.isoformat(),
            "last_updated_at": self.last_updated_at.isoformat(),
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
            "is_active": self.is_active,
            "version": self.version,
            "is_deleted": self.is_deleted,
        }

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, uid={self.uid}, is_active={self.is_active}, version={self.version})"
