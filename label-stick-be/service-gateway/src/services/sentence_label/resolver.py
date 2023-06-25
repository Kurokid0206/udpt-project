from fastapi.encoders import jsonable_encoder

from .dto import SentenceLabelInputDTO, SentenceLabelResponseDTO, StatusSentenceLabelResponseDTO
from ...configs.base import SENTENCE_SERVICE_URL
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod


async def resolve_create_sentence_label(sentence: SentenceLabelInputDTO) -> ResponseDTO[SentenceLabelResponseDTO]:
    url = f"{SENTENCE_SERVICE_URL}/create_sentence_label"
    data = jsonable_encoder(sentence)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[SentenceLabelResponseDTO](**response)


async def resolve_delete_sentence_label(id: int = None) -> ResponseDTO[StatusSentenceLabelResponseDTO]:
    url = f"{SENTENCE_SERVICE_URL}/delete_sentence_label/{id}"
    response = await call_api(url=url, method=HttpMethod.DELETE)
    return ResponseDTO[StatusSentenceLabelResponseDTO](**response)
