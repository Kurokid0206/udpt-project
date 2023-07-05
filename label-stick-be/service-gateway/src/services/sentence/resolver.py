from .dto import SentenceInputDTO, SentenceResponseDTO
from ..label_sentence.dto import LabelSentenceInputDTO, LabelSentenceResponseDTO
from ...utils.dto import ResponseDTO
from ...utils.rest_api import call_api, HttpMethod
from ...configs.base import LABEL_SERVICE_URL
from fastapi.encoders import jsonable_encoder


async def resolve_create_sentences(
    sentences: list[SentenceInputDTO],
) -> ResponseDTO[list[SentenceResponseDTO]]:
    url = f"{LABEL_SERVICE_URL}/sentence"
    data = jsonable_encoder(sentences)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[list[SentenceResponseDTO]](
        **{"data": [SentenceResponseDTO(**item) for item in response]}
    )


async def resolve_update_sentence(
    id: int,
    sentence: SentenceInputDTO,
) -> ResponseDTO[SentenceResponseDTO]:
    url = f"{LABEL_SERVICE_URL}/sentence/{id}"
    data = jsonable_encoder(sentence)
    response = await call_api(url=url, method=HttpMethod.PUT, json=data)
    return ResponseDTO[SentenceResponseDTO](**{"data": response})


async def resolve_get_sentences_by_ids(
    ids: list[int],
) -> ResponseDTO[list[SentenceResponseDTO]]:
    url = f"{LABEL_SERVICE_URL}/sentence/get-by-ids"
    data = jsonable_encoder(ids)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    return ResponseDTO[list[SentenceResponseDTO]](
        **{"data": [SentenceResponseDTO(**item) for item in response]}
    )


async def resolve_add_labels_to_sentence(
    input: LabelSentenceInputDTO,
) -> ResponseDTO[list[LabelSentenceResponseDTO]]:
    url = f"{LABEL_SERVICE_URL}/sentence/add-labels"
    data = jsonable_encoder(input)
    response = await call_api(url=url, method=HttpMethod.POST, json=data)
    print(response)
    return ResponseDTO[list[LabelSentenceResponseDTO]](
        **{"data": [LabelSentenceResponseDTO(**item) for item in response]}
    )


async def resolve_get_sentences_by_document_id(
    document_id: int,
) -> ResponseDTO[list[SentenceResponseDTO]]:
    url = f"{LABEL_SERVICE_URL}/sentence/get-by-document/{document_id}"
    response = await call_api(url=url, method=HttpMethod.GET)
    return ResponseDTO[list[SentenceResponseDTO]](
        **{"data": [SentenceResponseDTO(**item) for item in response]}
    )
