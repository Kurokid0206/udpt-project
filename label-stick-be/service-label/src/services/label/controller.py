from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import label_repository
from .schema import Label, LabelCreate, LabelUpdate
from ...database.sessions import get_session

router = APIRouter(prefix="/label", tags=["label"])


@router.get("/{id}", response_model=Label)
async def get_label(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.get(db=session, id=id)
    return label


@router.get("", response_model=list[Label])
async def get_list_label(
    page: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[Label]:
    skip = page * 100
    labels = label_repository.get_multi(db=session, skip=skip, limit=100)
    return labels


@router.post("", response_model=Label)
async def create_label(
    input: LabelCreate,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.create(session, obj_in=input)
    return label


@router.patch("/{id}", response_model=Label)
async def update_label(
    id: int,
    input: LabelUpdate,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.update(session, db_obj_id=id, obj_in=input)
    return label


@router.delete("/{id}", response_model=Label)
async def delete_label(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.remove(session, id=id)
    return label
