from typing import Optional
from strawberry.file_uploads import Upload
import strawberry
from enum import Enum


@strawberry.enum
class AssignmentTypeEnum(Enum):
    LABEL = "LABEL"
    REVIEW = "REVIEW"


@strawberry.type
class AssignmentResponseDTO:
    id: int
    name: str
    sentence_ids: list[int]
    user_id: int
    assign_type: AssignmentTypeEnum
    from_date: str
    to_date: str
    # create_at: str
    # create_at: str


@strawberry.input
class CreateAssignmentInputDTO:
    name: str
    sentence_ids: list[int]
    user_id: int
    assign_type: AssignmentTypeEnum
    from_date: str
    to_date: str


@strawberry.input
class UpdateAssignmentInputDTO:
    # id: int
    name: Optional[str]
    sentence_ids: Optional[list[int]]
    user_id: Optional[int]
    assign_type: Optional[AssignmentTypeEnum]
    from_date: Optional[str]
    to_date: Optional[str]


@strawberry.input
class AssignmentFilterInputDTO:
    user_id: Optional[int] = 1
    page: Optional[int] = 0
    limit: Optional[int] = 100
