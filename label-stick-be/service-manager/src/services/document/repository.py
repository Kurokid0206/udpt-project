from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Document, DocumentCreate, DocumentUpdate
from src.database.models import Document


class CRUDDocument(CRUDBase[Document, DocumentCreate, DocumentUpdate]):
    def get_by_project(
        self, db: Session, *, project_id: int = 0, skip: int, limit: int
    ) -> list[Document]:
        if project_id == 0:
            result = db.query(self.model).offset(skip).limit(limit).all()
            return result
        result = (
            db.query(self.model)
            .filter_by(project_id=project_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result


document_repository = CRUDDocument(Document)
