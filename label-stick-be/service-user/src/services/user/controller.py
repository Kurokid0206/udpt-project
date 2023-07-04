from fastapi import APIRouter, Depends
from .schema import User, UserCreate, UserUpdate, LoginDTO
from .repository import user_repository
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{username}", response_model=User)
async def get_user_by_code(username: str, session: AsyncSession = Depends(get_session)):
    user = user_repository.get_by_username(id=username, db=session)
    return user


@router.get("/", response_model=list[User], description="get all user")
async def get_user(session: AsyncSession = Depends(get_session)):
    users = user_repository.get_multi(db=session)
    return users


@router.post("/signup", status_code=200, response_model=User)
async def signup_user(
    user_data: UserCreate,
    session: AsyncSession = Depends(get_session),
) -> User:
    # return {"username": "string", "email": "string", "user_id": 0}
    user = user_repository.create(obj_in=user_data, db=session)
    return user


@router.post("/login", status_code=200, response_model=User)
async def login_user(
    login_data: LoginDTO,
    session: AsyncSession = Depends(get_session),
) -> User:
    user = user_repository.login(obj_in=login_data, db=session)
    return user
