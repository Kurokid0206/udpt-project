from enum import Enum
import strawberry


@strawberry.input
class SentenceInputDTO:
    name: str = None
    sentence: str = None
    document_id: int = None


@strawberry.type
class SentenceResponseDTO:
    id: int = None
    name: str = None
    sentence: str = None
    document_id: int = None


@strawberry.enum
class LabelStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CONFIRMED = "CONFIRMED"


@strawberry.input
class addLabelInputDTO:
    sentence_id: int = None
    label_id: int = None
    user_id: int = None
    status: LabelStatus = LabelStatus.IN_PROGRESS


@strawberry.type
class SentenceLabelResponseDTO:
    sentence_id: int = None
    label_id: int = None
    review_by: int = None
    status: LabelStatus = LabelStatus.IN_PROGRESS
