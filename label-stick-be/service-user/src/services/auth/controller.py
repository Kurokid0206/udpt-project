from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.sessions import get_session

router = APIRouter(prefix="/auth", tags=["auth"])

token_auth_scheme = HTTPBearer()  # 👈 new code


@router.get("/test")
async def test_auth(token: str = Depends(token_auth_scheme)):
    return {}


@router.post("/login")
async def login():
    return {}
