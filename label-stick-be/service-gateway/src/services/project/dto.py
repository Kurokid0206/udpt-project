import strawberry


@strawberry.input
class ProjectUserDTO:
    ids: list[int] = []
