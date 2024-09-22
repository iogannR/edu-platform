import uuid

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    password: str
    roles: list[str]
        

class UserRead(UserCreate):
    password: bytes
    id: uuid.UUID
    
    model_config = ConfigDict(
        from_attributes=True,
    )
    

class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None
    password: bytes | None = None
    roles: list[str] | None = None