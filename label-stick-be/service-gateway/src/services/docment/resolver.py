from .dto import CreateDocumentInputDTO, DocumentResponseDTO, UpdateDocumnetInputDTO
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import MANAGER_SERVICE_URL
import strawberry
from fastapi.encoders import jsonable_encoder


async def resolve_create_document(input: CreateDocumentInputDTO) -> ResponseDTO[DocumentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/document/create"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[DocumentResponseDTO](**{"data": DocumentResponseDTO(**response)})

async def resolve_update_document(input: UpdateDocumnetInputDTO) -> ResponseDTO[DocumentResponseDTO]:
    url = f"{MANAGER_SERVICE_URL}/document/update"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[DocumentResponseDTO](**{"data": DocumentResponseDTO(**response)})

async def resolve_delete_document(id: int) -> ResponseDTO[dict]:
    url = f"{MANAGER_SERVICE_URL}/document/delete"
    response = await call_api(url=url, method=HttpMethod.POST, json={"id": id})
    return ResponseDTO[dict](**{"data":response})


