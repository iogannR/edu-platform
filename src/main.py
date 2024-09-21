from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.database.manager import db_manager


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    await db_manager.dispose()
    
    
app = FastAPI(
    title="Educational Platform",
    lifespan=lifespan,
)

@app.get("/message")
async def send_message(message: str) -> dict:
    return {
        "message": message,
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )