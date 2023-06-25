from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum

Base = declarative_base()


class UserRoleEnum(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    USER_LV_1 = "USER_LV_1"
    USER_LV_2 = "USER_LV_2"
    USER_LV_3 = "USER_LV_3"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(ENUM(UserRoleEnum, name="user_role_enum"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

    # Relationship
    # tasks = relationship("UserTask", back_populates="user")
