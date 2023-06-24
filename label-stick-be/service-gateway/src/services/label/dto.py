import strawberry
from pydantic import BaseModel


@strawberry.type
class Labeler:
    name: str = None


@strawberry.input
class LabelerFilterDTO:
    name: str = None
