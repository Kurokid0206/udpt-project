from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.dialects.postgresql import ENUM, JSONB
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

    # Proxy
    projects = association_proxy("project_users", "projects")

    # Relationship
    assignments = relationship("Assignment", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    max_user = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    # project_type = Column(String(50), nullable=False)

    # Proxy
    users = association_proxy("project_users", "users")

    # Relationship
    documents = relationship("Document", back_populates="project")

    def __repr__(self):
        return f"<Project(id={self.id}, project_name={self.name}, users={self.users})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ProjectUser(Base):
    __tablename__ = "project_users"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationship
    projects = relationship("Project", backref="project_users")
    users = relationship("User", backref="project_users")

    def __repr__(self):
        return f"<ProjectUser(id={self.id}, project_id={self.project_id}, user_id={self.user_id})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class DocumentTypeEnum(str, Enum):
    QUESTION = "QUESTION"


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    document_url = Column(String(50))
    document_type = Column(
        ENUM(DocumentTypeEnum, name="document_type_enum"), nullable=False
    )
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationship
    project = relationship("Project", back_populates="documents")
    sentences = relationship("Sentence", back_populates="document")

    def __repr__(self):
        return f"<Document(id={self.id}, document_name={self.name})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Label(Base):
    __tablename__ = "labels"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Proxy
    sentences = association_proxy("label_sentences", "sentences")

    # # Relationship
    # sentences = relationship("LabelSentence", back_populates="labels")

    def __repr__(self):
        return f"<Label(id={self.id}, label_name={self.name})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Sentence(Base):
    __tablename__ = "sentences"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    sentence = Column(String(1000), nullable=False)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Proxy
    labels = association_proxy("label_sentences", "labels")

    # Relationship
    document = relationship("Document", back_populates="sentences")
    # labels = relationship("LabelSentence", back_populates="sentences")

    def __repr__(self):
        return f"<Sentence(id={self.id}, sentence_name={self.name})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class LabelSentenceStatusEnum(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    CONFIRMED = "CONFIRMED"


class LabelSentence(Base):
    __tablename__ = "label_sentences"
    id = Column(Integer, primary_key=True)
    sentence_id = Column(Integer, ForeignKey("sentences.id"), nullable=False)
    label_id = Column(Integer, ForeignKey("labels.id"), nullable=False)
    labeled_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    reviewed_by = Column(Integer, ForeignKey("users.id"))
    status = Column(
        ENUM(LabelSentenceStatusEnum, name="label_sentence_status_enum"),
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationship
    sentences = relationship("Sentence", backref="labels")
    labels = relationship("Label", backref="sentences")

    def __repr__(self):
        return f"<LabelSentence(id={self.id}, sentence_id={self.sentence_id}, label_id={self.label_id}, user_id={self.user_id})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class AssignmentTypeEnum(str, Enum):
    LABEL = "LABEL"
    REVIEW = "REVIEW"
    REVISE = "REVISE"


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    sentence_ids = Column(JSONB, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assign_type = Column(
        ENUM(AssignmentTypeEnum, name="assignment_type_enum"),
        nullable=False,
        server_default="LABEL",
    )
    from_date = Column(DateTime(timezone=True), nullable=False)
    to_date = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationship
    user = relationship("User", back_populates="assignments")

    def __repr__(self):
        return f"<Assignment(id={self.id}, assignment_name={self.name})>"

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
