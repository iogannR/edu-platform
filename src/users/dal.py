from sqlalchemy.ext.asyncio import AsyncSession

from core.dal.base import BaseSQLAlchemyDAL
from .model import User
from .schemas import UserCreate, UserUpdate, UserUpdatePartial


class UserSQLAlchemyDAL(
    BaseSQLAlchemyDAL[
        User, UserCreate, UserUpdate, UserUpdatePartial,
    ]
):
    """Class that represents User Data Access Layer"""
    
    def __init__(self, session: AsyncSession, model: User) -> None:
        super().__init__(session, User)
        
        
    async def update(
        self, 
        id_: int, 
        schema: UserUpdate | UserUpdatePartial,
        *,
        partial: bool = False,
    ) -> User:
        entity = await self._session.get(self._model, id_)
        data = schema.model_dump(exclude_unset=partial)
        data["password"] = hash_password(data["password"]) # type: ignore
        if entity:
            for key, value in data:
                setattr(entity, key, value)
            await self._session.commit()
            await self._session.refresh(entity)
            return entity
        else:
            return None
    
    
    async def get_by_username(self, username: str) -> User | None:
        user = await self._session.get(User, username)
        return user
    
    async def get_by_email(self, email: str) -> User | None:
        user = await self._session.get(User, email)
        return user