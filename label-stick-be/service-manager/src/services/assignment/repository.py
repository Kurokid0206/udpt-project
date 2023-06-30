from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Assignment, AssignmentCreate, AssignmentUpdate
from src.database.models import Assignment


class CRUDAssignment(CRUDBase[Assignment, AssignmentCreate, AssignmentUpdate]):
    def get_by_user_id(
        self,
        db: Session,
        user_id: int,
        skip: int,
        limit: int,
    ) -> list[Assignment]:
        results = (
            db.query(self.model)
            .filter_by(user_id=user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return results


assignment_repository = CRUDAssignment(Assignment)
