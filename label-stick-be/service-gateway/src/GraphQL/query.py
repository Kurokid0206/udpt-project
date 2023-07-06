from typing import Any, Optional
import strawberry

from ..utils.dto import ResponseDTO

# from ..services.label.dto import LabelerFilterDTO, Labeler

from ..services.project.dto import (
    ProjectResponseDTO,
    ProjectUserDTO,
    ProjectUserFilterDTO,
)
from ..services.document.dto import DocumentFilterInputDTO, DocumentResponseDTO
from ..services.assignment.dto import AssignmentFilterInputDTO, AssignmentResponseDTO
from ..services.label.dto import LabelResponseDTO
from ..services.sentence.dto import SentenceLabelResponseDTO, SentenceResponseDTO
from ..services.user.dto import UserResponseDTO

from ..services.project.resolver import (
    resolve_get_projects,
    resolve_get_projects_by_user,
)
from ..services.document.resolver import resolve_get_documents
from ..services.assignment.resolver import resolve_get_assignments
from ..services.label.resolver import resolve_get_labels
from ..services.sentence.resolver import (
    resolve_get_sentences_by_ids,
    resolve_get_sentences_by_document_id,
    resolve_get_sentence_labels,
)
from ..services.user.resolver import resolve_get_labelers


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
    ) -> ResponseDTO[list[UserResponseDTO]]:
        result = resolve_get_labelers()
        return result

    @strawberry.field
    def get_projects(
        self, filter: Optional[ProjectUserDTO] = None
    ) -> ResponseDTO[list[ProjectResponseDTO]]:
        result = resolve_get_projects(filter)
        return result

    @strawberry.field
    def get_projects_by_user_id(
        self, filter: ProjectUserFilterDTO
    ) -> ResponseDTO[list[ProjectResponseDTO]]:
        result = resolve_get_projects_by_user(filter)
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
    def get_sentences_by_ids(
        self, ids: list[int]
    ) -> ResponseDTO[list[SentenceResponseDTO]]:
        # TODO: allow get labels of sentence
        result = resolve_get_sentences_by_ids(ids)
        return result

    @strawberry.field
    def get_sentence_labels(
        self, sentence_id: int
    ) -> ResponseDTO[list[SentenceLabelResponseDTO]]:
        result = resolve_get_sentence_labels(sentence_id)
        return result

    @strawberry.field
    def get_labels(self) -> ResponseDTO[list[LabelResponseDTO]]:
        result = resolve_get_labels()
        return result

    @strawberry.field
    def get_sentences_by_document_id(
        self, document_id: int
    ) -> ResponseDTO[list[SentenceResponseDTO]]:
        result = resolve_get_sentences_by_document_id(document_id)
        return result

    @strawberry.field
    def find_sentence_by_key(self) -> HealthCheck:
        # TODO: allow get project id and document id
        return {}

    # note: 1 api for get label statistics
