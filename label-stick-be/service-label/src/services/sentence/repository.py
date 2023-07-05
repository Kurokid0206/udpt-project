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

    def get_by_document_id(self, db: Session, *, document_id: int) -> list[Sentence]:
        result = db.query(self.model).filter_by(document_id=document_id).all()
        return result

    def create_many(
        self, db: Session, *, obj_list: list[SentenceCreate]
    ) -> list[Sentence]:
        result = []
        for obj in obj_list:
            db_obj = self.model(**obj.dict())
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            result.append(db_obj)
        return result


sentence_repository = CRUDSentence(Sentence)
