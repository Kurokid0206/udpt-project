from fastapi import APIRouter, Depends, UploadFile, Form, File
from .schema import Document, DocumentCreate, DocumentUpdate
from .repository import document_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session
from ...utils.storage import put_object

router = APIRouter(prefix="/document", tags=["document"])


@router.get("", response_model=list[Document])
async def get_documents(
    project_id: int = 1,
    page: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
) -> list[Document]:
    skip = page * 100
    documents = document_repository.get_by_project(
        db=session, project_id=project_id, skip=skip, limit=limit
    )
    return documents


@router.get("/{id}", response_model=Document)
async def get_document(
    id: int = 0,
    session: AsyncSession = Depends(get_session),
) -> Document:
    document = document_repository.get(db=session, id=id)
    return document


@router.post("", response_model=Document)
async def create_document(
    input: DocumentCreate,
    session: AsyncSession = Depends(get_session),
) -> Document:
    try:
        # data = DocumentCreate.parse_raw(input)
        # file_url = put_object(key=data.project_id, file=file)
        # data.document_url = file_url
        document = document_repository.create(session, obj_in=input)

    except Exception as e:
        print(f"error: {e}")
        raise e
    return document


@router.patch("/{id}", response_model=Document)
async def update_document(
    id: int,
    input: DocumentUpdate,
    session: AsyncSession = Depends(get_session),
) -> Document:
    document = document_repository.update(session, db_obj_id=id, obj_in=input)
    return document


@router.delete("/{id}", response_model=Document)
async def delete_document(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> Document:
    document = document_repository.remove(session, id=id)
    return document
