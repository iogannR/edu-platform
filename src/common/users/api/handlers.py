import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from common.users.dal import UserSQLAlchemyDAL
from common.users.schemas import (
    UserRead, UserCreate, UserUpdate, UserUpdatePartial,
)
from .dependencies import get_user_dal


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserRead])
async def get_all_users(
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.get_all()


@router.get("/{id_}")
async def get_user_by_id(
    id_: uuid.UUID,
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
) -> UserRead | None:
    return await user_dal.get_by_id(id_)


@router.post("/create", response_model=UserRead)
async def create_user(
    schema: UserCreate,
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.create(schema)


@router.put("/update/{id_}", response_model=UserRead)
async def update_user(
    id_: uuid.UUID,
    schema: UserUpdate,
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.update(id_, schema)


@router.patch("/update/{id_}", response_model=UserRead)
async def update_user_partial(
    id_: uuid.UUID,
    schema: UserUpdate,
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.update(id_, schema, partial=True)


@router.delete("/delete/{id_}", response_model=None)
async def delete_user(
    id_: uuid.UUID,
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.delete(id_)