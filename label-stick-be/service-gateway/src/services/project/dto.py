from typing import Optional
import strawberry


@strawberry.input
class CreateProjectDTO:
    name: str = None
    description: str = None
    max_user: int = 10


@strawberry.input
class UpdateProjectDTO:
    name: Optional[str] = None
    description: Optional[str] = None
    max_user: Optional[int] = 10


@strawberry.type
class ProjectResponseDTO:
    id: int = None
    name: str = None
    description: str = None
    max_user: int = 10


@strawberry.input
class ProjectUserDTO:
    ids: list[int] = None
    page: int = 0


@strawberry.input
class AddProjectUserDTO:
    project_id: int = None
    user_ids: list[int] = None
