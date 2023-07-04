from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

# from db.models import Person
from .schema import LabelSentence, LabelSentenceCreate, LabelSentenceUpdate
from src.database.models import LabelSentence


class CRUDLabelSentence(
    CRUDBase[LabelSentence, LabelSentenceCreate, LabelSentenceUpdate]
):
    def get_by_sentence_id(
        self, db: Session, *, sentence_id: int, skip: int = 0, limit: int = 100
    ) -> list[LabelSentence]:
        result = (
            db.query(self.model)
            .filter(self.model.sentence_id == sentence_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result


label_sentence_repository = CRUDLabelSentence(LabelSentence)
