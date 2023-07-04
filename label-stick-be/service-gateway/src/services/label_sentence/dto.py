from enum import Enum

import strawberry


@strawberry.enum
class LabelSentenceStatusEnum(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CONFIRMED = "CONFIRMED"


@strawberry.input
class LabelSentenceInputDTO:
    id: int = None
    label_ids: list[int] = None
    status: LabelSentenceStatusEnum = LabelSentenceStatusEnum.IN_PROGRESS
    user_id: int = None


@strawberry.type
class LabelSentenceResponseDTO:
    id: int = None
    sentence_id: int = None
    label_id: int = None
    labeled_by: int = None
    reviewed_by: int = None
    status: str = None
