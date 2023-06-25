import strawberry
from enum import Enum


@strawberry.input
class LoginDTO:
    username: str = None
    password: str = None


@strawberry.type
class LoginResponseDTO:
    access_token: str = None
    refresh_token: str = None


@strawberry.enum
class UserRoleEnum(Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    USER_LV_1 = "USER_LV_1"
    USER_LV_2 = "USER_LV_2"
    USER_LV_3 = "USER_LV_3"


@strawberry.input
class UserInputDTO:
    username: str = None
    email: str = None
    password: str = None
    first_name: str = None
    last_name: str = None
    role: UserRoleEnum = UserRoleEnum.USER_LV_1


@strawberry.type
class UserResponseDTO:
    user_id: str = None
    username: str = None
    email: str = None
