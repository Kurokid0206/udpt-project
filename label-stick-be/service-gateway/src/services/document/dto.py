from enum import Enum
from typing import Optional
from strawberry.file_uploads import Upload
import strawberry


@strawberry.input
class DocumentFilterInputDTO:
    project_id: Optional[int] = 0
    page: Optional[int] = 0
    limit: Optional[int] = 100


@strawberry.enum
class DocumentTypeEnum(Enum):
    TEXT = "TEXT"
    QUESTION = "QUESTION"
    TRANSLATE = "TRANSLATE"
    ENTITY = "ENTITY"
    SYNONYMOUS = "SYNONYMOUS"
    TRUE_FALSE = "TRUE_FALSE"
    ANSWER = "ANSWER"


@strawberry.type
class DocumentResponseDTO:
    id: int
    name: str
    document_url: str
    document_type: DocumentTypeEnum
    project_id: int
    # create_at: str
    # create_at: str


@strawberry.input
class CreateDocumentInputDTO:
    name: str
    document_type: DocumentTypeEnum
    document_url: str
    project_id: int
    # file: Upload


@strawberry.input
class UpdateDocumentInputDTO:
    # id: int
    name: Optional[str]
    file: Optional[Upload]
    document_type: Optional[DocumentTypeEnum]
