from .dto import LoginDTO, UserInputDTO, UserResponseDTO
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import USER_SERVICE_URL
import strawberry
from fastapi.encoders import jsonable_encoder


async def resolve_signup(user: UserInputDTO) -> ResponseDTO[UserResponseDTO]:
    url = f"{USER_SERVICE_URL}/signup"
    data = jsonable_encoder(user)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[UserResponseDTO](**{"data": UserResponseDTO(**response)})

    print("=====================")
    print(response)
    print("=====================")
    # result = {"data": UserResponseDTO(**response)}
    return ResponseDTO[UserResponseDTO](**response)


async def resolve_update_profile(user: UserInputDTO) -> ResponseDTO[UserResponseDTO]:
    url = f"{USER_SERVICE_URL}/update_profile"
    data = jsonable_encoder(user)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[UserResponseDTO](**response)


async def resolve_login(user: LoginDTO) -> ResponseDTO[UserResponseDTO]:
    url = f"{USER_SERVICE_URL}/user/login"
    data = jsonable_encoder(user)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[UserResponseDTO](**{"data": UserResponseDTO(**response)})
