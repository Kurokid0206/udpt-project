import strawberry
from pydantic import BaseModel


@strawberry.input
class LabelInputDTO(BaseModel):
    name: str = None


@strawberry.type
class LabelResponseDTO:
    id: int = None
    name: str = None
