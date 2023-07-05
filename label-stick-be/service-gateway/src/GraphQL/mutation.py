import strawberry

from ..services.assignment.dto import (
    AssignmentResponseDTO,
    CreateAssignmentInputDTO,
    UpdateAssignmentInputDTO,
)
from ..services.assignment.resolver import (
    resolve_create_assignment,
    resolve_update_assignment,
)
from ..services.document.dto import (
    CreateDocumentInputDTO,
    DocumentResponseDTO,
    UpdateDocumentInputDTO,
)
from ..services.document.resolver import (
    resolve_create_document,
    resolve_delete_document,
    resolve_update_document,
)
from ..services.label.dto import LabelInputDTO, LabelResponseDTO
from ..services.label.resolver import (
    resolve_create_label,
    resolve_update_label,
    resolve_delete_label,
)
from ..services.label_sentence.dto import (
    LabelSentenceInputDTO,
    LabelSentenceResponseDTO,
)
from ..services.label_sentence.resolver import (
    resolve_create_label_sentence,
    resolve_delete_label_sentence,
)
from ..services.project.dto import (
    CreateProjectDTO,
    ProjectResponseDTO,
    UpdateProjectDTO,
    AddProjectUserDTO,
)
from ..services.project.resolver import (
    resolve_create_project,
    resolve_update_project,
    resolve_delete_project,
    resolve_add_user_to_project,
)
from ..services.sentence.dto import (
    SentenceInputDTO,
    SentenceResponseDTO,
)
from ..services.sentence.resolver import (
    resolve_add_labels_to_sentence,
    resolve_create_sentences,
    resolve_update_sentence,
)
from ..services.user.dto import (
    UserResponseDTO,
    LoginDTO,
    UserInputDTO,
    LoginResponseDTO,
)
from ..services.user.resolver import (
    resolve_signup,
    resolve_update_profile,
    resolve_login,
)
from ..utils.dto import ResponseDTO, StatusResponseDTO


@strawberry.type
class Mutation:
    # Common
    @strawberry.mutation
    def login(self, input: LoginDTO) -> ResponseDTO[UserResponseDTO]:
        result = resolve_login(input)
        return result

    @strawberry.mutation
    def signup(self, input: UserInputDTO) -> ResponseDTO[UserResponseDTO]:
        result = resolve_signup(input)
        return result

    @strawberry.mutation
    def update_profile(self, input: UserInputDTO) -> ResponseDTO[UserResponseDTO]:
        result = resolve_update_profile(input)
        return result

    # Admin
    @strawberry.mutation
    def delete_user(self, id: str) -> ResponseDTO[StatusResponseDTO]:
        return {}

    # Manager
    @strawberry.mutation
    def create_project(
        self,
        input: CreateProjectDTO,
    ) -> ResponseDTO[ProjectResponseDTO]:
        result = resolve_create_project(input)
        return result

    @strawberry.mutation
    def update_project(
        self,
        id: int,
        input: UpdateProjectDTO,
    ) -> ResponseDTO[ProjectResponseDTO]:
        result = resolve_update_project(id, input)
        return result

    @strawberry.mutation
    def delete_project(self, id: int) -> ResponseDTO[ProjectResponseDTO]:
        result = resolve_delete_project(id)
        return result

    @strawberry.mutation
    def add_user_to_project(
        self, input: AddProjectUserDTO
    ) -> ResponseDTO[ProjectResponseDTO]:
        result = resolve_add_user_to_project(input)
        return result

    # Document
    @strawberry.mutation
    def create_document(
        self,
        input: CreateDocumentInputDTO,
    ) -> ResponseDTO[DocumentResponseDTO]:
        result = resolve_create_document(input)
        return result

    @strawberry.mutation
    def update_document(
        self,
        id: int,
        input: UpdateDocumentInputDTO,
    ) -> ResponseDTO[DocumentResponseDTO]:
        result = resolve_update_document(id, input)
        return result

    @strawberry.mutation
    def delete_document(self, id: int) -> ResponseDTO[StatusResponseDTO]:
        result = resolve_delete_document(id)
        return result

    @strawberry.mutation
    def create_assignment(
        self, input: CreateAssignmentInputDTO
    ) -> ResponseDTO[AssignmentResponseDTO]:
        result = resolve_create_assignment(input)
        return result

    @strawberry.mutation
    def update_assignment(
        self, id: int, input: UpdateAssignmentInputDTO
    ) -> ResponseDTO[UserResponseDTO]:
        result = resolve_update_assignment(id, input)
        return result

    # TODO: create list of sentences.
    # 1. upload file
    # 2. split into sentences
    # 3. call create sentences from list
    @strawberry.mutation
    def create_sentences(
        self, input: list[SentenceInputDTO]
    ) -> ResponseDTO[list[SentenceResponseDTO]]:
        result = resolve_create_sentences(input)
        return result

    @strawberry.mutation
    def update_sentence(
        self, id: int, input: SentenceInputDTO
    ) -> ResponseDTO[SentenceResponseDTO]:
        # TODO: only manager can update sentence
        result = resolve_update_sentence(id, input)
        return result

    # Labeler
    @strawberry.mutation
    def create_label_sentence(
        self, input: LabelSentenceInputDTO
    ) -> ResponseDTO[LabelSentenceResponseDTO]:
        result = resolve_create_label_sentence(input)
        return result

    @strawberry.mutation
    def delete_label_sentence(self, id: int) -> ResponseDTO[StatusResponseDTO]:
        result = resolve_delete_label_sentence(id)
        return result

    # Label
    @strawberry.mutation
    def create_label(self, input: LabelInputDTO) -> ResponseDTO[LabelResponseDTO]:
        result = resolve_create_label(input)
        return result

    @strawberry.mutation
    def update_label(
        self, id: int, input: LabelInputDTO
    ) -> ResponseDTO[StatusResponseDTO]:
        result = resolve_update_label(id, input)
        return result

    @strawberry.mutation
    def delete_label(self, id: int) -> ResponseDTO[StatusResponseDTO]:
        result = resolve_delete_label(id)
        return result

    @strawberry.mutation
    def add_labels_to_sentence(
        self, input: LabelSentenceInputDTO
    ) -> ResponseDTO[list[LabelSentenceResponseDTO]]:
        result = resolve_add_labels_to_sentence(input)
        return result
