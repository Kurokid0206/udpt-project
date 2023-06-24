import strawberry
from pydantic import BaseModel


@strawberry.input
class LoginDTO(BaseModel):
    username: str = None
    password: str = None


@strawberry.type
class LoginResponseDTO(BaseModel):
    access_token: str = None
    refresh_token: str = None


@strawberry.input
class UserInputDTO(LoginDTO):
    username: str = None
    password: str = None


@strawberry.type
class UserResponseDTO(BaseModel):
    username: str = None
    role: str = None
