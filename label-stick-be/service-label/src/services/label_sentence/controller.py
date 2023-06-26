from fastapi import APIRouter, Depends
from .schema import LabelSentence, LabelSentenceCreate, LabelSentenceUpdate
from .repository import label_sentence_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/sentence", tags=["label_sentence"])


@router.post("/create_label_sentence", response_model=LabelSentence)
async def create_sentence(
    input: LabelSentenceCreate,
    session: AsyncSession = Depends(get_session),
) -> LabelSentence:
    sentence = label_sentence_repository.create(session, obj_in=input)
    return sentence


@router.patch("/update_label_sentence/:id", response_model=LabelSentence)
async def update_sentence(
    id: int,
    input: LabelSentenceUpdate,
    session: AsyncSession = Depends(get_session),
) -> LabelSentence:
    sentence = label_sentence_repository.update(session, db_obj_id=id, obj_in=input)
    return sentence


@router.delete("/delete_label_sentence/:id", response_model=LabelSentence)
async def delete_sentence(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> LabelSentence:
    sentence = label_sentence_repository.remove(session, id=id)
    return sentence