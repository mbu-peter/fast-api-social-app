from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, EmailStr, Field


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Userdetails(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: Userdetails

    class Config:
        from_attributes = True


class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginCredentials(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class Like(BaseModel):
    post_id: int
    dir:  Annotated[int, Field(strict=True,  le=1)]


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True
