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


user_repository = CRUDUser(User)
