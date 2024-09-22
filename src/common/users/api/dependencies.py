from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.users.dal import UserSQLAlchemyDAL
from core.database.manager import db_manager


def get_user_dal(
    session: AsyncSession = Depends(db_manager.sessiion_dependency),
) -> UserSQLAlchemyDAL:
    return UserSQLAlchemyDAL(session)