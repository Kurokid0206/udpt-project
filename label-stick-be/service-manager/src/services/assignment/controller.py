from fastapi import APIRouter, Depends
from .schema import Assignment, AssignmentCreate, AssignmentUpdate
from .repository import assignment_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session
from ...utils.mail import send_mail, SendMailDTO

router = APIRouter(prefix="/assignment", tags=["assignment"])


@router.get("", response_model=list[Assignment])
async def get_assignments(
    user_id: int = 0,
    page: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
) -> list[Assignment]:
    skip = page * limit
    assignments = assignment_repository.get_by_user_id(
        db=session, user_id=user_id, skip=skip, limit=limit
    )

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
    input: AssignmentCreate,
    session: AsyncSession = Depends(get_session),
) -> Assignment:
    # data = AssignmentCreate.parse_raw(input)
    assignment = assignment_repository.create(session, obj_in=input)
    user = assignment.user
    mail_data = {
        "to_email": user.email,
        "subject": assignment.name,
        "username": user.username,
        "project_name": "demo",
        "task_type": assignment.assign_type,
        "deadline": str(assignment.to_date),
    }
    mail_data = SendMailDTO(**mail_data)
    await send_mail(mail_data)
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
