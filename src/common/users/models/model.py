from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

from core.database.model import Base
from common.users.models.enum import PlatformRole

if TYPE_CHECKING:
    from common.articles.models import Article
    

class User(Base):
    username: Mapped[str] = mapped_column(String(65), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(85), unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    password: Mapped[str]
    roles: Mapped[list[PlatformRole]] = mapped_column(ARRAY(String), nullable=False)
    
    articles_: Mapped[list["Article"]] = relationship(back_populates="user_")
          
    @property
    def is_admin(self) -> bool:
        return PlatformRole.ROLE_PLATFORM_ADMIN in self.roles
