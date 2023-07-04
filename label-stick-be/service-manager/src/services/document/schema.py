from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class DocumentTypeEnum(str, Enum):
    QUESTION = "QUESTION"
    TEXT = "TEXT"
    TRANSLATE = "TRANSLATE"
    ENTITY = "ENTITY"
    SYNONYMOUS = "SYNONYMOUS"
    TRUE_FALSE = "TRUE_FALSE"
    ANSWER = "ANSWER"


class DocumentBase(BaseModel):
    name: str = Field(alias="name")
    document_type: DocumentTypeEnum = Field(
        DocumentTypeEnum.QUESTION, alias="document_type"
    )
    document_url: str = Field(None, alias="document_url")
    project_id: int = Field(alias="project_id")


class DocumentCreate(DocumentBase):
    name: str = Field(alias="name")
    document_url: str = Field(None, alias="document_url")
    document_type: DocumentTypeEnum = Field(
        DocumentTypeEnum.QUESTION, alias="document_type"
    )
    project_id: int = Field(alias="project_id")

    class Config:
        allow_population_by_field_name = True


class DocumentUpdate(DocumentBase):
    name: str = Field(alias="name")
    document_type: DocumentTypeEnum = Field(
        DocumentTypeEnum.QUESTION, alias="document_type"
    )
    project_id: int = Field(alias="project_id")

    class Config:
        allow_population_by_field_name = True


class DocumentDelete(DocumentBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class DocumentInDBBase(DocumentBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Document(DocumentInDBBase):
    ...
