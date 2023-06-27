from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Project, ProjectCreate, ProjectUpdate
from src.database.models import Project, ProjectUser


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def add_users_to_project(
        self, db: Session, *, project_id: int, user_ids: list[int]
    ) -> Project:
        for user_id in user_ids:
            db_obj = ProjectUser(project_id=project_id, user_id=user_id)
            db.add(db_obj)

        db_obj = db.query(Project).filter_by(id=project_id).first()
        db.commit()
        db.refresh(db_obj)
        return db_obj


project_repository = CRUDProject(Project)
