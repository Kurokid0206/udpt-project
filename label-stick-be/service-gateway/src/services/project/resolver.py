from .dto import (
    CreateProjectDTO,
    ProjectResponseDTO,
    ProjectUserDTO,
    ProjectUserFilterDTO,
    UpdateProjectDTO,
)
from ...utils.dto import ResponseDTO, StatusResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import MANAGER_SERVICE_URL
from fastapi.encoders import jsonable_encoder


async def resolve_get_projects(
    filter: ProjectUserDTO = None,
) -> ResponseDTO[list[ProjectResponseDTO]]:
    url = f"{MANAGER_SERVICE_URL}/project"
    response = await call_api(
        url=url,
        method=HttpMethod.GET,
        params=jsonable_encoder(filter),
    )
    return ResponseDTO[list[response]](
        **{
            "status_code": 200,
            "message": "success",
            "data": [ProjectResponseDTO(**item) for item in response],
        }
    )


async def resolve_create_project(
    input: CreateProjectDTO,
) -> ResponseDTO[ProjectResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/project"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[ProjectResponseDTO](**{"data": ProjectResponseDTO(**response)})

    print("=====================")
    print(response)
    print("=====================")
    # result = {"data": UserResponseDTO(**response)}
    return ResponseDTO[UserResponseDTO](**response)


async def resolve_update_project(
    id: int,
    input: UpdateProjectDTO,
) -> ResponseDTO[ProjectResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/project/{id}"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.PATCH, json=data)
    return ResponseDTO[ProjectResponseDTO](**{"data": ProjectResponseDTO(**response)})


async def resolve_delete_project(id: int) -> StatusResponseDTO:
    url = f"{MANAGER_SERVICE_URL}/project/{id}"
    response = await call_api(url=url, method=HttpMethod.DELETE)
    return ResponseDTO[StatusResponseDTO](**response)


async def resolve_add_user_to_project(
    input: ProjectUserDTO,
) -> ResponseDTO[ProjectResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/project/add-users"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[ProjectResponseDTO](**{"data": ProjectResponseDTO(**response)})


async def resolve_get_projects_by_user(
    filter: ProjectUserFilterDTO,
) -> ResponseDTO[list[ProjectResponseDTO]]:
    url = f"{MANAGER_SERVICE_URL}/project/by-user/{filter.user_id}"
    response = await call_api(
        url=url,
        method=HttpMethod.GET,
        params=jsonable_encoder(filter),
    )
    return ResponseDTO[list[ProjectResponseDTO]](
        **{
            "status_code": 200,
            "message": "success",
            "data": [ProjectResponseDTO(**item) for item in response],
        }
    )
