from typing import Optional
import strawberry

from ..utils.dto import ResponseDTO
from ..services.label.dto import LabelerFilterDTO, Labeler

from ..services.project.dto import ProjectUserDTO


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
        filter: Optional[LabelerFilterDTO] = None,
    ) -> ResponseDTO[list[Labeler]]:
        return {}

    @strawberry.field
    def get_projects(self, filter: Optional[ProjectUserDTO] = None) -> HealthCheck:
        return {}

    @strawberry.field
    def get_documents(self) -> HealthCheck:
        # TODO: allow get status of assignment in document
        return {}

    # Labeler
    @strawberry.field
    def get_assignments(self) -> HealthCheck:
        return {}

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
