import strawberry
from pydantic import BaseModel


@strawberry.input
class ProjectUserDTO:
    ids: list[int] = []
