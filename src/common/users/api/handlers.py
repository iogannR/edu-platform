from typing import Annotated

from fastapi import APIRouter, Depends

from common.users.dal import UserSQLAlchemyDAL
from common.users.schemas import UserRead
from .dependencies import get_user_dal


router = APIRouter(tags=["Users"])


@router.get("/users", response_model=list[UserRead])
async def get_all_users(
    user_dal: Annotated[UserSQLAlchemyDAL, Depends(get_user_dal)],
):
    return await user_dal.get_all()