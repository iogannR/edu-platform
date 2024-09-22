from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.articles.dal import ArticleSQLAlchemyDAL
from core.database.manager import db_manager


def get_article_dal(
    session: AsyncSession = Depends(db_manager.sessiion_dependency),
) -> ArticleSQLAlchemyDAL:
    return ArticleSQLAlchemyDAL(session)