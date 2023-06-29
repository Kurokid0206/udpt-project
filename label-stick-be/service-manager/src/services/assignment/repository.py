from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Assignment, AssignmentCreate, AssignmentUpdate
from src.database.models import Assignment


class CRUDAssignment(CRUDBase[Assignment, AssignmentCreate, AssignmentUpdate]):
    pass


assignment_repository = CRUDAssignment(Assignment)
