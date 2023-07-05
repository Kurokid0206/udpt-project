from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import User, UserCreate, UserUpdate, LoginDTO
from src.database.models import User


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def login(self, *, obj_in: LoginDTO, db: Session) -> User:
        db_obj = (
            db.query(self.model)
            .filter_by(username=obj_in.username, password=obj_in.password)
            .first()
        )
        if not db_obj:
            return None

        return db_obj

    def get_labelers(self, *, db: Session) -> list[User]:
        list_role = ["USER_LV_1", "USER_LV_2", "USER_LV_3"]
        db_obj = db.query(self.model).filter(self.model.role.in_(list_role)).all()
        if not db_obj:
            return []

        return db_obj


user_repository = CRUDUser(User)
