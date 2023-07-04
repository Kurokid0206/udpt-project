from typing import Optional

from pydantic import BaseModel, Field


class LabelSentenceBase(BaseModel):
    sentence_id: int = Field(alias="sentence_id")
    label_id: int = Field(alias="label_id")
    labeled_by: int = Field(alias="labeled_by")
    reviewed_by: Optional[int] = Field(None, alias="reviewed_by")
    status: str = Field(alias="status")


class LabelSentenceCreate(LabelSentenceBase):
    sentence_id: int = Field(alias="sentence_id")
    label_id: int = Field(alias="label_id")
    labeled_by: int = Field(alias="labeled_by")
    reviewed_by: int = Field(alias="reviewed_by")
    status: str = Field(alias="status")

    class Config:
        allow_population_by_field_name = True


class LabelSentenceUpdate(LabelSentenceBase):
    sentence_id: Optional[int] = Field(alias="sentence_id")
    label_id: Optional[int] = Field(alias="label_id")
    labeled_by: Optional[int] = Field(alias="labeled_by")
    reviewed_by: Optional[int] = Field(alias="reviewed_by")
    status: Optional[str] = Field(alias="status")

    class Config:
        allow_population_by_field_name = True


class LabelSentenceDelete(LabelSentenceBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class LabelSentenceInDBBase(LabelSentenceBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class LabelSentence(LabelSentenceInDBBase):
    ...
