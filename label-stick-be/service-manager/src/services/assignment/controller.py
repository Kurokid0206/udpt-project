from fastapi import APIRouter, Depends, UploadFile, Form, File
from .schema import Assignment, AssignmentCreate, AssignmentUpdate
from .repository import assignment_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session
from ...utils.storage import put_object

router = APIRouter(prefix="/assignment", tags=["assignment"])

@router.get("", response_model=list[Assignment])
async def get_assignments(
    page: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[Assignment]:
    skip = page * 100
    assignments = assignment_repository.get_multi(db=session, skip=skip, limit=100)
    return assignments


@router.get("/{id}", response_model=Assignment)
async def get_assignment(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> Assignment:
    assignment = assignment_repository.get(db=session, id=id)
    return assignment


@router.post("", response_model=Assignment)
async def create_assignment(
    input: str = Form(...),
    session: AsyncSession = Depends(get_session),
) -> Assignment:
    data = AssignmentCreate.parse_raw(input)
    assignment = assignment_repository.create(session, obj_in=data)
    return assignment


@router.patch("/{id}", response_model=Assignment)
async def update_assignment(
    id: int,
    input: AssignmentUpdate,
    session: AsyncSession = Depends(get_session),
) -> Assignment:
    assignment = assignment_repository.update(session, db_obj_id=id, obj_in=input)
    return assignment


@router.delete("/{id}", response_model=Assignment)
async def delete_assignment(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Assignment:
    assignment = assignment_repository.remove(session, id=id)
    return assignment
