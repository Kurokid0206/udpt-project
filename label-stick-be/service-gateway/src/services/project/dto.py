import strawberry
from pydantic import BaseModel


@strawberry.input
class ProjectUserDTO(BaseModel):
    ids: list[int] = []
