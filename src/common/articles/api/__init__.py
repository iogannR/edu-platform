from fastapi import APIRouter

from .handlers import router as article_router


router = APIRouter()
router.include_router(article_router, prefix="/articles")