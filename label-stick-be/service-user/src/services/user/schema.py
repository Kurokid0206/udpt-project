from pydantic import BaseModel, Field
from typing import Optional, Any, List
from enum import Enum


class UserBase(BaseModel):
    username: str = Field(alias="username")
    email: str = Field(alias="email")


class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserCreate(UserBase):
    username: str = Field(alias="username")
    email: str = Field(alias="email")
    password: str = Field(alias="password")
    first_name: str = Field(alias="first_name")
    last_name: str = Field(alias="last_name")
    role: UserRoleEnum = Field(alias="role")

    class Config:
        allow_population_by_field_name = True


class UserUpdate(UserBase):
    username: str = Field(alias="username")
    email: str = Field(alias="email")
    password: str = Field(alias="password")

    class Config:
        allow_population_by_field_name = True


class UserDelete(UserBase):
    username: str = Field(alias="username")

    class Config:
        allow_population_by_field_name = True


#############################
class UserInDBBase(UserBase):
    id: Optional[int] = Field(alias="user_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class User(UserInDBBase):
    ...
