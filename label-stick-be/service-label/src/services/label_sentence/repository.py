from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import LabelSentence, LabelSentenceCreate, LabelSentenceUpdate
from src.database.models import LabelSentence


class CRUDLabelSentence(CRUDBase[LabelSentence, LabelSentenceCreate, LabelSentenceUpdate]):
    pass


label_sentence_repository = CRUDLabelSentence(LabelSentence)
