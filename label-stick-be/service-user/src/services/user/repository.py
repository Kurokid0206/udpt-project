from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import User, UserCreate, UserUpdate
from src.database.models import User


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


user_repository = CRUDUser(User)
