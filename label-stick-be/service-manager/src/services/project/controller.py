from fastapi import APIRouter, Depends
from .schema import Project, ProjectCreate, ProjectUpdate
from .repository import project_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/project", tags=["project"])


@router.post("", response_model=Project)
async def create_project(
    input: ProjectCreate,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.create(session, obj_in=input)
    return project


@router.patch("/:id", response_model=Project)
async def create_project(
    id: int,
    input: ProjectCreate,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.update(session, db_obj_id=id, obj_in=input)
    return project
