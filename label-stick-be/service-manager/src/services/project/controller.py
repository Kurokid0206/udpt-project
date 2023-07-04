from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .schema import Project, ProjectCreate, ProjectUpdate
from .repository import project_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/project", tags=["project"])


@router.get("", response_model=list[Project])
async def get_projects(
    page: int = 0,
    session: AsyncSession = Depends(get_session),
) -> list[Project]:
    skip = page * 100
    projects = project_repository.get_multi(db=session, skip=skip, limit=100)
    return projects


@router.get("/{id}", response_model=Project)
async def get_project(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.get(db=session, id=id)
    return project
    response = {**project.dict(), "users": [user.dict() for user in project.users]}
    return response


@router.get("/by-user/{user_id}", response_model=list[Project])
async def get_user_project(
    user_id: int = 0,
    page: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
) -> list[Project]:
    projects = project_repository.get_user_project(
        db=session, user_id=user_id, skip=page * limit, limit=limit
    )
    # print("====================")
    # print(projects)
    # print(type(projects))
    # print("====================")

    return [Project(**project.dict()) for project in projects]


@router.post("", response_model=Project)
async def create_project(
    input: ProjectCreate,
    session: AsyncSession = Depends(get_session),
) -> Project:
    print("input", input)
    project = project_repository.create(session, obj_in=input)
    return project


@router.patch("/{id}", response_model=Project)
async def create_project(
    id: int,
    input: ProjectUpdate,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.update(session, db_obj_id=id, obj_in=input)
    return project


@router.delete("/{id}", response_model=Project)
async def create_project(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.remove(session, id=id)
    return project


class ProjectUsersDTO(BaseModel):
    project_id: int
    user_ids: list[int]


@router.post("/add-users", response_model=Project)
async def add_user_to_project(
    input: ProjectUsersDTO,
    session: AsyncSession = Depends(get_session),
) -> Project:
    project = project_repository.add_users_to_project(session, **input.dict())
    return project
