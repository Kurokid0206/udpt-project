from fastapi import APIRouter, Depends
from .schema import Label, LabelCreate, LabelUpdate
from .repository import label_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/label", tags=["label"])


@router.post("/create_label", response_model=Label)
async def create_label(
    input: LabelCreate,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.create(session, obj_in=input)
    return label


@router.patch("/update_label/:id", response_model=Label)
async def update_label(
    id: int,
    input: LabelUpdate,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.update(session, db_obj_id=id, obj_in=input)
    return label


@router.delete("/delete_label/:id", response_model=Label)
async def delete_label(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Label:
    label = label_repository.remove(session, id=id)
    return label
