from .dto import LabelInputDTO, LabelResponseDTO
from ...utils.dto import ResponseDTO, StatusResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import MANAGER_SERVICE_URL
from fastapi.encoders import jsonable_encoder


async def resolve_create_label(
    input: LabelInputDTO,
) -> ResponseDTO[LabelResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/label"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[LabelResponseDTO](**response)


async def resolve_update_label(
    id: int,
    input: LabelInputDTO,
) -> ResponseDTO[LabelResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/label/{id}"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[LabelResponseDTO](**response)


async def resolve_delete_label(id: int) -> StatusResponseDTO:
    url = f"{MANAGER_SERVICE_URL}/label/{id}"
    response = await call_api(url=url, method=HttpMethod.DELETE)
    return ResponseDTO[StatusResponseDTO](**response)