from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import sentence_repository
from .schema import Sentence, SentenceCreate, SentenceUpdate
from ...database.sessions import get_session

router = APIRouter(prefix="/sentence", tags=["sentence"])


@router.get("/{id}", response_model=Sentence)
async def get_sentence(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> Sentence:
    sentence = sentence_repository.get(db=session, id=id)
    return sentence


@router.get("", response_model=list[Sentence])
async def get_list_sentence(
    page: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[Sentence]:
    skip = page * 100
    sentences = sentence_repository.get_multi(db=session, skip=skip, limit=100)
    return sentences


@router.post("/get-by-ids", response_model=list[Sentence])
async def get_list_sentence(
    session: AsyncSession = Depends(get_session),
    ids: list[int] = [],
    page: int = 0,
    limit: int = 100,
) -> list[Sentence]:
    skip = page * limit
    sentences = sentence_repository.get_by_ids(
        db=session, ids=ids, skip=skip, limit=limit
    )
    return sentences


@router.post("", response_model=List[Sentence])
async def create_sentences(
    input: List[SentenceCreate],
    session: AsyncSession = Depends(get_session),
) -> List[Sentence]:
    sentences = sentence_repository.create_many(session, obj_list=input)
    return sentences


@router.patch("/{id}", response_model=Sentence)
async def update_sentence(
    id: int,
    input: SentenceUpdate,
    session: AsyncSession = Depends(get_session),
) -> Sentence:
    sentence = sentence_repository.update(session, db_obj_id=id, obj_in=input)
    return sentence


@router.delete("/{id}", response_model=Sentence)
async def delete_sentence(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Sentence:
    sentence = sentence_repository.remove(session, id=id)
    return sentence
