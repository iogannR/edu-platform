import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from common.articles.dal import ArticleSQLAlchemyDAL
from common.articles.schemas import (
    ArticleRead, ArticleCreate, ArticleUpdate, ArticleUpdatePartial,
)
from .dependencies import get_article_dal

router = APIRouter(tags=["Articles"])


@router.get("/", response_model=list[ArticleRead])
async def get_all_users(
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
):
    return await user_dal.get_all()


@router.get("/{id_}")
async def get_user_by_id(
    id_: uuid.UUID,
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
) -> ArticleRead | None:
    return await user_dal.get_by_id(id_)


@router.post("/create", response_model=ArticleRead)
async def create_user(
    schema: ArticleCreate,
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
):
    return await user_dal.create(schema)


@router.put("/update/{id_}", response_model=ArticleRead)
async def update_user(
    id_: uuid.UUID,
    schema: ArticleUpdate,
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
):
    return await user_dal.update(id_, schema)


@router.patch("/update/{id_}", response_model=ArticleRead)
async def update_user_partial(
    id_: uuid.UUID,
    schema: ArticleUpdatePartial,
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
):
    return await user_dal.update(id_, schema, partial=True)


@router.delete("/delete/{id_}", response_model=None)
async def delete_user(
    id_: uuid.UUID,
    user_dal: Annotated[ArticleSQLAlchemyDAL, Depends(get_article_dal)],
):
    return await user_dal.delete(id_)