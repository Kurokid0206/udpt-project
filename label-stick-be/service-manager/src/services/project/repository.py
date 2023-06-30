from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Project, ProjectCreate, ProjectUpdate
from src.database.models import Project, ProjectUser, User


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

    def get_user_project(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> list[Project]:
        user = db.query(User).filter_by(id=user_id).offset(skip).limit(limit).first()
        return user.projects


project_repository = CRUDProject(Project)
