from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import Task, TaskCreate, TaskUpdate
from src.database.models import Task


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    pass


task_repository = CRUDTask(Task)
