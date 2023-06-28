from enum import Enum

import strawberry


@strawberry.enum
class LabelSentenceStatusEnum(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CONFIRMED = "CONFIRMED"


@strawberry.input
class LabelSentenceInputDTO:
    sentence_id: int = None
    label_id: int = None
    status: LabelSentenceStatusEnum = LabelSentenceStatusEnum.IN_PROGRESS
    updated_by: int = None


@strawberry.type
class LabelSentenceResponseDTO:
    id: int = None
    sentence_id: int = None
    label_id: int = None
    updated_by: int = None
