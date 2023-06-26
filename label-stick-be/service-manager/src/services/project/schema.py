from pydantic import BaseModel, Field
from typing import Optional, Any, List


class ProjectBase(BaseModel):
    # id: str = Field(alias="id")
    name: str = Field(alias="name")
    max_user: str = Field(alias="max_user")


class ProjectCreate(ProjectBase):
    name: str = Field(alias="name")
    max_user: int = Field(alias="max_user")

    class Config:
        allow_population_by_field_name = True


class ProjectUpdate(ProjectBase):
    name: Optional[str] = Field(alias="name")
    max_user: Optional[int] = Field(alias="max_user")

    class Config:
        allow_population_by_field_name = True


class ProjectDelete(ProjectBase):
    id: int = Field(alias="id")

    class Config:
        allow_population_by_field_name = True


#############################
class ProjectInDBBase(ProjectBase):
    id: Optional[int] = Field(alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Project(ProjectInDBBase):
    ...
