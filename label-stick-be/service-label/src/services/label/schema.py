from ast import List
from typing import Optional

from pydantic import BaseModel, Field


class LabelBase(BaseModel):
    name: str = Field(alias="name")


class LabelCreate(LabelBase):
    name: str = Field(alias="name")

    class Config:
        allow_population_by_field_name = True


class LabelUpdate(LabelBase):
    name: Optional[str] = Field(alias="name")

    class Config:
        allow_population_by_field_name = True


class LabelDelete(LabelBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class LabelInDBBase(LabelBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Label(LabelInDBBase):
    ...
