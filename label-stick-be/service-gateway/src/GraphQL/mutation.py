from ..services.assignment.resolver import (
    resolve_create_assignment,
    resolve_update_assignment,
)
from ..services.assignment.dto import (
    AssignmentResponseDTO,
    CreateAssignmentInputDTO,
    UpdateAssignmentInputDTO,
)
from ..services.document.resolver import (
    resolve_create_document,
    resolve_delete_document,
    resolve_update_document,
)
from ..services.document.dto import (
    CreateDocumentInputDTO,
    DocumentResponseDTO,
    UpdateDocumentInputDTO,
)
import strawberry
from strawberry.file_uploads import Upload

from ..utils.dto import ResponseDTO
from ..services.user.dto import (
    UserResponseDTO,
    LoginDTO,
    UserInputDTO,
    LoginResponseDTO,
)

from ..services.sentence.dto import (
    SentenceInputDTO,
    SentencesInputDTO,
    SentenceResponseDTO,
)

from ..services.sentence_label.dto import (
    SentenceLabelInputDTO,
    SentenceLabelResponseDTO,
    StatusSentenceLabelResponseDTO,
)

from ..services.user.resolver import resolve_signup, resolve_update_profile
from ..services.sentence.resolver import (
    resolve_create_sentences,
    resolve_update_sentence,
)
from ..services.sentence_label.resolver import (
    resolve_create_sentence_label,
    resolve_delete_sentence_label,
)


@strawberry.type
class Mutation:
    # Common
    @strawberry.mutation
    def login(self, input: LoginDTO) -> ResponseDTO[LoginResponseDTO]:
        return {}

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
    def delete_user(self, id: str) -> ResponseDTO[UserResponseDTO]:
        return {}

    # Manager
    @strawberry.mutation
    def create_project(
        self,
        name: str,
        description: str,
    ) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def update_project(
        self,
        id: str,
        name: str,
        description: str,
    ) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def delete_project(self, id: str) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def add_user_to_project(self) -> ResponseDTO[UserResponseDTO]:
        return {}

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
    def delete_document(self, id: int) -> ResponseDTO[dict]:
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
        self, input: SentencesInputDTO
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
    def create_sentence_label(
        self, input: SentenceLabelInputDTO
    ) -> ResponseDTO[SentenceLabelResponseDTO]:
        result = resolve_create_sentence_label(input)
        return result

    @strawberry.mutation
    def delete_sentence_label(
        self, id: int
    ) -> ResponseDTO[StatusSentenceLabelResponseDTO]:
        result = resolve_delete_sentence_label(id)
        return result
