from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import Sentence, SentenceCreate, SentenceUpdate
from src.database.models import Sentence


class CRUDSentence(CRUDBase[Sentence, SentenceCreate, SentenceUpdate]):
    def get_by_ids(
        self, db: Session, *, ids: list[int], skip: int, limit: int
    ) -> list[Sentence]:
        result = (
            db.query(self.model)
            .filter(self.model.id.in_(ids))
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result


sentence_repository = CRUDSentence(Sentence)
