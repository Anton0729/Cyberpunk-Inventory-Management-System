from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category: str
    quantity: int
    price: float


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    quantity: int
    price: float


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
