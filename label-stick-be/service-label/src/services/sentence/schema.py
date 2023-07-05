from typing import Optional

from pydantic import BaseModel, Field


class SentenceLabelsDTO(BaseModel):
    label_ids: list[int] = []
    id: int
    user_id: int
    status: str


class SentenceBase(BaseModel):
    name: str = Field(alias="name")
    sentence: str = Field(alias="sentence")
    document_id: int = Field(alias="document_id")


class SentenceCreate(SentenceBase):
    name: str = Field(alias="name")
    sentence: str = Field(alias="sentence")
    document_id: int = Field(alias="document_id")

    class Config:
        allow_population_by_field_name = True


class SentenceUpdate(SentenceBase):
    name: Optional[str] = Field(alias="name")
    sentence: Optional[str] = Field(alias="sentence")
    document_id: Optional[int] = Field(alias="document_id")

    class Config:
        allow_population_by_field_name = True


class SentenceDelete(SentenceBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class SentenceInDBBase(SentenceBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Sentence(SentenceInDBBase):
    ...
