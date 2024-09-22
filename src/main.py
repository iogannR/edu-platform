from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.database.manager import db_manager
from common.users.api import router as api_user_router
from common.articles.api import router as api_article_router

@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    await db_manager.dispose()
    
    
app = FastAPI(
    title="Educational Platform",
    lifespan=lifespan,
)
app.include_router(api_user_router)
app.include_router(api_article_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )