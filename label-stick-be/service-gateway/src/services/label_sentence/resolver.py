from fastapi.encoders import jsonable_encoder

from .dto import (
    LabelSentenceInputDTO,
    LabelSentenceResponseDTO,
)
from ...configs.base import SENTENCE_SERVICE_URL
from ...utils.dto import ResponseDTO, StatusResponseDTO
from ...utils.rest_api import call_api, HttpMethod


async def resolve_create_label_sentence(
    sentence: LabelSentenceInputDTO,
) -> ResponseDTO[LabelSentenceResponseDTO]:
    url = f"{SENTENCE_SERVICE_URL}/create_label_sentence"
    data = jsonable_encoder(sentence)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[LabelSentenceResponseDTO](**response)


async def resolve_delete_label_sentence(
    id: int = None,
) -> ResponseDTO[StatusResponseDTO]:
    url = f"{SENTENCE_SERVICE_URL}/delete_label_sentence/{id}"
    response = await call_api(url=url, method=HttpMethod.DELETE)
    return ResponseDTO[StatusResponseDTO](**response)
