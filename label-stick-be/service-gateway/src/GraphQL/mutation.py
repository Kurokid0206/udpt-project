import strawberry
from strawberry.file_uploads import Upload

from ..utils.dto import ResponseDTO
from ..services.user.dto import (
    UserResponseDTO,
    LoginDTO,
    UserInputDTO,
    LoginResponseDTO,
)

from ..services.user.resolver import resolve_signup, resolve_update_profile


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
    def create_document(self, file: Upload) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def update_document(self, id: str, file: Upload) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def delete_document(self, id: str) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def create_assignment(self) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def update_assignment(self) -> ResponseDTO[UserResponseDTO]:
        return {}

    # TODO: create list of sentences.
    # 1. upload file
    # 2. split into sentences
    # 3. call create sentences from list
    @strawberry.mutation
    def create_sentences(
        self,
        document_id: int,
        sentences: list[str] = [],
    ) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def update_sentence(
        self,
        id: int,
        sentence: str,
    ) -> ResponseDTO[UserResponseDTO]:
        # TODO: only manager can update sentence
        return {}

    # Labeler
    @strawberry.mutation
    def create_sentence_label(
        self,
        sentence_id: int,
        label_id: int,
    ) -> ResponseDTO[UserResponseDTO]:
        return {}

    @strawberry.mutation
    def delete_sentence_label(
        self,
        sentence_id: int,
        label_id: int,
    ) -> ResponseDTO[UserResponseDTO]:
        return {}
