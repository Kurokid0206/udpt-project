import strawberry
from enum import Enum

@strawberry.enum
class SentenceLabelStatusEnum(Enum):
    DONE = "DONE"
    DELETED = "DELETED"

@strawberry.input
class SentenceLabelInputDTO:
    sentence_id: int = None
    label_id: int = None
    status: SentenceLabelStatusEnum = SentenceLabelStatusEnum.DONE
    updated_by: int = None


@strawberry.type
class SentenceLabelResponseDTO:
    id: int = None
    sentence_id: int = None
    label_id: int = None
    updated_by: int = None
