from src.database.crud import CRUDBase
from src.database.models import Label

# from db.models import Person
from .schema import LabelCreate, LabelUpdate


class CRUDLabel(CRUDBase[Label, LabelCreate, LabelUpdate]):
    pass


label_repository = CRUDLabel(Label)
