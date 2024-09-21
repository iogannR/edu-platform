from sqlalchemy.ext.asyncio import AsyncSession
from core.dal.base import BaseSQLAlchemyDAL
from .model import Article
from .schemas import ArticleCreate, ArticleUpdate, ArticleUpdatePartial


class ArticleSQLAlchemyDAL(
    BaseSQLAlchemyDAL[
        Article, ArticleCreate, ArticleUpdate, ArticleUpdatePartial,
    ]
):
    """Class that represents Article Data Access Layer"""
    
    def __init__(self, session: AsyncSession, model: Article) -> None:
        super().__init__(session, Article)
        
    async def get_by_title(self, title: str) -> Article | None:
        article = await self._session.get(Article, title)
        return article