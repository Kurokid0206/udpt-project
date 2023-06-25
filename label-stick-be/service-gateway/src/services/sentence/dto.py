import strawberry


@strawberry.input
class SentencesInputDTO:
    document_id: int = None
    contents: list[str] = []


@strawberry.input
class SentenceInputDTO:
    document_id: int = None
    content: str = None

class UpdateSentenceInputDTO:
    id: int = None
    document_id: int = None
    content: str = None


@strawberry.type
class SentenceResponseDTO:
    id: int = None
    document_id: int = None
    content: str = None
