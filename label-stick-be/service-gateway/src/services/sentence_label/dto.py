from enum import Enum

import strawberry


@strawberry.enum
class SentenceLabelStatusEnum(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CONFIRMED = "CONFIRMED"


@strawberry.input
class SentenceLabelInputDTO:
    sentence_id: int = None
    label_id: int = None
    status: SentenceLabelStatusEnum = SentenceLabelStatusEnum.IN_PROGRESS
    updated_by: int = None


@strawberry.type
class SentenceLabelResponseDTO:
    id: int = None
    sentence_id: int = None
    label_id: int = None
    updated_by: int = None
