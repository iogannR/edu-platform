import uuid

from pydantic import BaseModel, ConfigDict, EmailStr


class ArticleCreate(BaseModel):
    title: str
    body: str
    user_id: uuid.UUID
        

class ArticleRead(ArticleCreate):
    id: uuid.UUID
    
    model_config = ConfigDict(
        from_attributes=True,
    )
    

class ArticleUpdate(ArticleCreate):
    pass


class ArticleUpdatePartial(BaseModel):
    title: str | None = None
    body: str | None = None
    user_id: uuid.UUID | None = None