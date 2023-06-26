from pydantic import BaseModel
import strawberry


@strawberry.input
class ProjectUserDTO(BaseModel):
    ids: list[int] = []
