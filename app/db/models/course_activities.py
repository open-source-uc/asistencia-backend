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

from app.db.models import *
from app.db.base import Base
from app.db.dependencies import get_db_session
from app.settings import settings


class CourseActivity(Base):
    """Represents a course activity entity."""

    __tablename__ = "course_activity"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    event_type: Mapped[Integer] = mapped_column(Integer, nullable=False, default=0)
    slug: Mapped[String] = mapped_column(String, nullable=False)
    course_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("course.id"), nullable=False
    )
    date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    course_activity_records = relationship(
        "CourseStudentActivityRecord", backref=backref("course_activity")
    )
