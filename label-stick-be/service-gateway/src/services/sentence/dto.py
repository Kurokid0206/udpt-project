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
