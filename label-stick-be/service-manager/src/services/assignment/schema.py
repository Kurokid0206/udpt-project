from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class AssignmentTypeEnum(str, Enum):
    LABEL = "LABEL"
    REVIEW = "REVIEW"
    REVISE = "REVISE"


class AssignmentBase(BaseModel):
    name: str = Field(alias='name')
    sentence_ids: list[int] = Field(alias='sentence_ids') 
    user_id: int = Field(alias='user_id') 
    assign_type: AssignmentTypeEnum = Field( AssignmentTypeEnum.LABEL, alias='assign_type')
    from_date: str = Field(alias='from_date')
    to_date: str = Field(alias='to_date')


class AssignmentCreate(AssignmentBase):
    name: str = Field(alias='name')
    sentence_ids: list[int] = Field(alias='sentence_ids') 
    user_id: int = Field(alias='user_id') 
    assign_type: AssignmentTypeEnum = Field(AssignmentTypeEnum.LABEL, alias='assign_type')
    from_date: str = Field(alias='from_date')
    to_date: str = Field(alias='to_date')

    class Config:
        allow_population_by_field_name = True


class AssignmentUpdate(AssignmentBase):
    name: str = Field(alias='name')
    sentence_ids: list[int] = Field(alias='sentence_ids') 
    user_id: int = Field(alias='user_id') 
    assign_type: AssignmentTypeEnum = Field(AssignmentTypeEnum.LABEL, alias='assign_type')
    from_date: str = Field(alias='from_date')
    to_date: str = Field(alias='to_date')

    class Config:
        allow_population_by_field_name = True


class AssignmentDelete(AssignmentBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class AssignmentInDBBase(AssignmentBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Assignment(AssignmentInDBBase):
    ...
