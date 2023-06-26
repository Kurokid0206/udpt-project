from typing import Generic, TypeVar
import strawberry

DataT = TypeVar("DataT")


@strawberry.type
class ResponseDTO(Generic[DataT]):
    status_code: int = 200
    message: str = "OK"
    data: DataT = None


@strawberry.type
class StatusResponseDTO:
    status_code: int = 200
    message: str = "OK"
