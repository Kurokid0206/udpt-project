from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Assignment, AssignmentCreate, AssignmentUpdate
from src.database.models import Assignment


class CRUDAssignment(CRUDBase[Assignment, AssignmentCreate, AssignmentUpdate]):
    def get_by_user_id(
        self,
        db: Session,
        user_id: int = 0,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Assignment]:
        if user_id == 0 or user_id == 1:
            results = db.query(self.model).offset(skip).limit(limit).all()
            return results
        results = (
            db.query(self.model)
            .filter_by(user_id=user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return results


assignment_repository = CRUDAssignment(Assignment)
