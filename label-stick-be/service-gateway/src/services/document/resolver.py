from .dto import (
    CreateDocumentInputDTO,
    DocumentFilterInputDTO,
    DocumentResponseDTO,
    UpdateDocumentInputDTO,
)
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import MANAGER_SERVICE_URL
from fastapi.encoders import jsonable_encoder


async def resolve_get_documents(
    filter: DocumentFilterInputDTO,
) -> ResponseDTO[DocumentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/document"
    data = jsonable_encoder(filter)
    response = await call_api(url=url, method=HttpMethod.GET, params=data)
    return ResponseDTO[list[DocumentResponseDTO]](
        **{"data": [DocumentResponseDTO(**item) for item in response]}
    )


async def resolve_create_document(
    input: CreateDocumentInputDTO,
) -> ResponseDTO[DocumentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/document"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[DocumentResponseDTO](**{"data": DocumentResponseDTO(**response)})


async def resolve_update_document(
    id: int,
    input: UpdateDocumentInputDTO,
) -> ResponseDTO[DocumentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/document/{id}"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.PATCH, json=data)
    return ResponseDTO[DocumentResponseDTO](**{"data": DocumentResponseDTO(**response)})


async def resolve_delete_document(id: int) -> ResponseDTO[dict]:
    url = f"{MANAGER_SERVICE_URL}/document/{id}"
    response = await call_api(url=url, method=HttpMethod.DELETE)
    return ResponseDTO[dict](**{"data": response})
