from typing import Any, Optional
import strawberry

from ..utils.dto import ResponseDTO

# from ..services.label.dto import LabelerFilterDTO, Labeler

from ..services.project.dto import ProjectResponseDTO, ProjectUserDTO
from ..services.document.dto import DocumentFilterInputDTO, DocumentResponseDTO
from ..services.assignment.dto import AssignmentFilterInputDTO, AssignmentResponseDTO
from ..services.project.resolver import resolve_get_projects
from ..services.document.resolver import resolve_get_documents
from ..services.assignment.resolver import resolve_get_assignments


@strawberry.type
class HealthCheck:
    status: int = 200
    message: str = "OK"


@strawberry.type
class Query:
    @strawberry.field
    def health_check(self) -> HealthCheck:
        return HealthCheck()

    # Admin

    # Manager
    @strawberry.field
    def get_labelers(
        self,
        # filter: Optional[LabelerFilterDTO] = None,
    ) -> ResponseDTO[list[HealthCheck]]:
        return {}

    @strawberry.field
    def get_projects(
        self, filter: Optional[ProjectUserDTO] = None
    ) -> ResponseDTO[list[ProjectResponseDTO]]:
        result = resolve_get_projects(filter)
        return result

    @strawberry.field
    def get_documents(
        self, filter: Optional[DocumentFilterInputDTO] = None
    ) -> ResponseDTO[list[DocumentResponseDTO]]:
        # TODO: allow get status of assignment in document
        result = resolve_get_documents(filter)
        return result

    # Labeler
    @strawberry.field
    def get_assignments(
        self, filter: Optional[AssignmentFilterInputDTO] = None
    ) -> ResponseDTO[list[AssignmentResponseDTO]]:
        result = resolve_get_assignments(filter)
        return result

    @strawberry.field
    def get_sentences(self) -> HealthCheck:
        # TODO: allow get labels of sentence
        return {}

    # @strawberry.field
    # def get_labels(self, filter: Optional[LabelFilterDTO]):
    #     return {}

    @strawberry.field
    def find_sentence_by_key(self) -> HealthCheck:
        # TODO: allow get project id and document id
        return {}

    # note: 1 api for get label statistics
