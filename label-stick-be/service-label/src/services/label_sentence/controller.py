from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import label_sentence_repository
from .schema import LabelSentence, LabelSentenceCreate, LabelSentenceUpdate
from ...database.sessions import get_session

router = APIRouter(prefix="/sentence", tags=["label_sentence"])


@router.get("/get_label_sentence/{id}", response_model=LabelSentence)
async def get_label_sentence(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> LabelSentence:
    label_sentence = label_sentence_repository.get(db=session, id=id)
    return label_sentence


@router.get("/get_list_label_sentence", response_model=list[LabelSentence])
async def get_list_label_sentence(
    page: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[LabelSentence]:
    skip = page * 100
    label_sentences = label_sentence_repository.get_multi(
        db=session, skip=skip, limit=100
    )
    return label_sentences


@router.get("/get_list_label_sentence/{id}", response_model=list[LabelSentence])
async def get_list_label_of_sentence(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[LabelSentence]:
    label_sentences = label_sentence_repository.get_by_column(
        db=session, column="sentence_id", value=id
    )
    return label_sentences


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
