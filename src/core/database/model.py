import uuid

from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)
from sqlalchemy.dialects.postgresql import UUID

from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    
    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4,
    )
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    