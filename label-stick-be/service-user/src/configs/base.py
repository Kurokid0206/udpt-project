import os
from typing import List, Union, Optional
from pydantic import BaseSettings, AnyHttpUrl, validator, EmailStr
from pathlib import Path


def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    server = os.getenv("POSTGRES_SERVER", "103.176.179.83")
    db = os.getenv("POSTGRES_DB", "postgres")
    return f"postgresql://{user}:{password}@{server}/{db}"


class Settings(BaseSettings):
    APP_TITLE: str = os.getenv("BACKEND_TITLE")
    APP_VERSION: str = os.getenv("BACKEND_VERSION")
    APP_HOST: str = os.getenv("DOMAIN")
    APP_PORT: int = os.getenv("BACKEND_PORT")

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: str = get_url()

    # FIRST USER ACCOUNT
    FIRST_SUPERUSER_EMAIL: EmailStr = os.getenv("TEST_USER_EMAIL")
    FIRST_SUPERUSER_PASSWORD: str = os.getenv("TEST_USER_PASSWORD")

    class Config:
        case_sensitive = True


settings = Settings()
