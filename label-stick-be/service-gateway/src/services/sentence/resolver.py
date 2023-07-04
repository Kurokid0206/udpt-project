from .dto import SentenceInputDTO, SentenceResponseDTO
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import LABEL_SERVICE_URL
from fastapi.encoders import jsonable_encoder


async def resolve_create_sentences(
    sentences: list[SentenceInputDTO],
) -> ResponseDTO[list[SentenceResponseDTO]]:
    url = f"{LABEL_SERVICE_URL}/create_sentences"
    data = jsonable_encoder(sentences)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[list[SentenceResponseDTO]](**response)


async def resolve_update_sentence(
    id: int,
    sentence: SentenceInputDTO,
) -> ResponseDTO[SentenceResponseDTO]:
    url = f"{LABEL_SERVICE_URL}/update_sentence/{id}"
    data = jsonable_encoder(sentence)
    response = await call_api(url=url, method=HttpMethod.PUT, json=data)
    return ResponseDTO[SentenceResponseDTO](**response)
