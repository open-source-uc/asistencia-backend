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
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.models import *
from app.db.base import Base
from app.db.dependencies import get_db_session
from app.settings import settings


class CourseStudentActivityRecord(Base):
    """Represents a course student activity record entity."""

    __tablename__ = "course_student_activity_record"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    student_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("student.id"), nullable=False
    )
    course_activity_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("course_activity.id"), nullable=False
    )
