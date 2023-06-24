from fastapi import APIRouter, Depends
from .schema import Task, TaskCreate, TaskUpdate
from .repository import task_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/:id", response_model=Task)
async def get_task_by_id(id: str, session: AsyncSession = Depends(get_session)):
    task = task_repository.get(id=id, db=session)
    return task


@router.get("/", response_model=list[Task], description="get all task")
async def get_task(session: AsyncSession = Depends(get_session)):
    tasks = task_repository.get_multi(db=session)
    return tasks


@router.post("/", status_code=200, response_model=Task)
def create_task(task_data: TaskCreate, session: AsyncSession = Depends(get_session)):
    task = task_repository.create(obj_in=task_data, db=session)
    return task


@router.post("/assign")
async def assign_task():
    return {}


@router.put("/")
def update_task():
    return {}
