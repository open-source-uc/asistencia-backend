# type: ignore
import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    DateTime,
    String,
    ForeignKey,
    types,
    func,
    UUID,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base import Base
from app.db.dependencies import get_db_session
from app.settings import settings


class Course(Base):
    """Represents a course entity."""

    __tablename__ = "course"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    name: Mapped[String] = mapped_column(String, nullable=False)
    archived: Mapped[Boolean] = mapped_column(Boolean, nullable=False, default=False)

    course_activities = relationship("CourseActivity", backref=backref("course"))
    students = relationship("Student", backref=backref("course"))
