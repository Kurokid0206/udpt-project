from typing import List

from fastapi import APIRouter, Depends
from .schema import Sentence, SentenceCreate, SentenceUpdate
from .repository import sentence_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/sentence", tags=["sentence"])


@router.post("/create_sentences", response_model=List[Sentence])
async def create_sentences(
    input: List[SentenceCreate],
    session: AsyncSession = Depends(get_session),
) -> List[Sentence]:
    sentences = sentence_repository.create_many(session, obj_list=input)
    return sentences


@router.patch("/update_sentence/:id", response_model=Sentence)
async def update_sentence(
    id: int,
    input: SentenceUpdate,
    session: AsyncSession = Depends(get_session),
) -> Sentence:
    sentence = sentence_repository.update(session, db_obj_id=id, obj_in=input)
    return sentence


@router.delete("/delete_sentence/:id", response_model=Sentence)
async def delete_sentence(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Sentence:
    sentence = sentence_repository.remove(session, id=id)
    return sentence