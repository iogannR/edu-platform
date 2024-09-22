from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.model import Base

if TYPE_CHECKING:
    from common.users.models import User


class Article(Base):
    title: Mapped[str] = mapped_column(String(65), nullable=False)
    body: Mapped[str] = mapped_column(Text)
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user_: Mapped[User] = relationship(back_populates="articles_")
    
