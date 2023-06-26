from typing import Optional
from pydantic import BaseModel
import strawberry


@strawberry.input
class CreateProjectDTO(BaseModel):
    name: str = None
    description: str = None
    max_user: int = 10


@strawberry.input
class UpdateProjectDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    max_user: Optional[int] = 10


@strawberry.type
class ProjectResponseDTO:
    id: int = None
    name: str = None
    description: str = None
    max_user: int = 10


@strawberry.input
class ProjectUserDTO(BaseModel):
    ids: list[int] = []
