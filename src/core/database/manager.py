from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from core.config import settings


class DatabaseManager:
    def __init__(self) -> None:
        self.async_engine: AsyncEngine = create_async_engine(
            str(settings.db.url),
            echo=settings.db.echo,
            pool_size=settings.db.pool_size,
            max_overflow=settings.db.max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
        
    async def dispose(self) -> None:
        await self.async_engine.dispose()
        
    async def sessiion_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            
            
db_manager = DatabaseManager()