from typing import TypeVar, Generic

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.model import Base

M = TypeVar("M", bound=Base) # SQLAlchemy ORM model
C = TypeVar("C", bound=BaseModel) # pydantic create schema
U = TypeVar("U", bound=BaseModel) # pydantic update schema
P = TypeVar("P", bound=BaseModel) # pydantic partial update schema


class BaseSQLAlchemyDAL(Generic[M, C, U, P]):
    """
    Base DAL class, from which other DAL classes should be inherited
    """
    
    def __init__(self, session: AsyncSession, model: type[M]) -> None:
        self._session = session
        self._model = model
    
    async def create(self, schema: C) -> M:
        entity = self._model(**schema.model_dump())
        self._session.add(entity)
        await self._session.commit()
        await self._session.refresh(entity)
        return entity

    async def get_by_id(self, id_: int) -> M | None:
        entity = await self._session.get(self._model, id_)
        return entity
    
    async def get_all(self) -> list[M]:
        result: Result = await self._session.execute(
            select(self._model).order_by(self._model.id),
        )
        return list(result.scalars().all())
    
    async def update(
        self, 
        id_: int, 
        schema: U | P,
        *,
        partial: bool = False,
    ) -> M:
        entity = await self._session.get(self._model, id_)
        if entity:
            for key, value in schema.model_dump(exclude_none=partial).items():
                setattr(entity, key, value)
            await self._session.commit()
            await self._session.refresh(entity)
            return entity
        else:
            return None
        
    async def delete(self, id_: int) -> None:
        entity = await self._session.get(self._model, id_)
        if entity:
            await self._session.delete(entity)
            await self._session.commit()
        else:
            return None