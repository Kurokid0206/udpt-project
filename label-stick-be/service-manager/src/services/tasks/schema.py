from pydantic import BaseModel, Field
from typing import Optional, Any, List
from enum import Enum


class TaskBase(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")


class TaskStatusEnum(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskCreate(TaskBase):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    # status: TaskStatusEnum = Field(alias="status", default=TaskStatusEnum.PENDING)

    class Config:
        allow_population_by_field_name = True


class TaskUpdate(TaskBase):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    status: TaskStatusEnum = Field(alias="status")

    class Config:
        allow_population_by_field_name = True


#############################
class TaskInDBBase(TaskBase):
    id: Optional[int] = Field(alias="Task_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Task(TaskInDBBase):
    ...
