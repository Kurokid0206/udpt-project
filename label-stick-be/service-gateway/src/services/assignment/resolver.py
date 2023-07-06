from .dto import (
    AssignmentFilterInputDTO,
    CreateAssignmentInputDTO,
    AssignmentResponseDTO,
    UpdateAssignmentInputDTO,
)
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import MANAGER_SERVICE_URL
import strawberry
from fastapi.encoders import jsonable_encoder


async def resolve_get_assignments(
    input: AssignmentFilterInputDTO,
) -> ResponseDTO[list[AssignmentResponseDTO]]:
    url = f"{MANAGER_SERVICE_URL}/assignment"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.GET, params=data)
    return ResponseDTO[AssignmentResponseDTO](
        **{"data": [AssignmentResponseDTO(**item) for item in response]}
    )


async def resolve_create_assignment(
    input: CreateAssignmentInputDTO,
) -> ResponseDTO[AssignmentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/assignment"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[AssignmentResponseDTO](
        **{"data": AssignmentResponseDTO(**response)}
    )


async def resolve_update_assignment(
    id: int,
    input: UpdateAssignmentInputDTO,
) -> ResponseDTO[AssignmentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/assignment/{id}"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.PATCH, json=data)
    return ResponseDTO[AssignmentResponseDTO](
        **{"data": AssignmentResponseDTO(**response)}
    )
