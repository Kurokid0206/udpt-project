from typing import Optional
from strawberry.file_uploads import Upload
import strawberry



@strawberry.enum
class DocumentTypeEnum:
    TEXT = "TEXT"
    QUESTION = "QUESTION"
    TRANSLATE = "TRANSLATE"
    ENTITY = "ENTITY"
    SYNONYMOUS = "SYNONYMOUS"
    TRUEFALSE = "TRUEFALSE"
    ANSWER = "ANSWER"

@strawberry.type
class DocumentResponseDTO:
    id: int
    name: str
    document_url: str
    document_type: DocumentTypeEnum
    project_id: int
    create_at: str
    create_at: str

@strawberry.input
class CreateDocumentInputDTO:
    name: str
    document_type: DocumentTypeEnum
    project_id: int
    file: Upload

@strawberry.input
class UpdateDocumnetInputDTO:
    id: int
    name: Optional[str]
    file: Optional[Upload]
    document_type: Optional[DocumentTypeEnum]
