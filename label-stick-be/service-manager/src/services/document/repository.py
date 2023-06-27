from typing import Any, Dict, Union
from src.database.crud import CRUDBase
from sqlalchemy.orm import Session

from .schema import Document, DocumentCreate, DocumentUpdate
from src.database.models import Document


class CRUDDocument(CRUDBase[Document, DocumentCreate, DocumentUpdate]):
    pass


document_repository = CRUDDocument(Document)
