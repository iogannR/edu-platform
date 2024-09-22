from sqlalchemy.ext.asyncio import AsyncSession

from core.dal.base import BaseSQLAlchemyDAL
from .models.model import User
from .schemas import UserCreate, UserUpdate, UserUpdatePartial


class UserSQLAlchemyDAL(
    BaseSQLAlchemyDAL[
        User, UserCreate, UserUpdate, UserUpdatePartial,
    ]
):
    """Class that represents User Data Access Layer"""
    
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User) 

    
    async def get_by_username(self, username: str) -> User | None:
        user = await self._session.get(User, username)
        return user
    
    async def get_by_email(self, email: str) -> User | None:
        user = await self._session.get(User, email)
        return user