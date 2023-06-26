from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import Sentence, SentenceCreate, SentenceUpdate
from src.database.models import Sentence


class CRUDSentence(CRUDBase[Sentence, SentenceCreate, SentenceUpdate]):
    pass


sentence_repository = CRUDSentence(Sentence)
