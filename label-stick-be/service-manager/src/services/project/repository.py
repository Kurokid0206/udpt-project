from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import Project, ProjectCreate, ProjectUpdate
from src.database.models import Project


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    pass


project_repository = CRUDProject(Project)
