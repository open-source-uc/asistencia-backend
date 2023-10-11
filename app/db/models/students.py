# type: ignore
import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Boolean, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base import Base
from app.db.dependencies import get_db_session
from app.settings import settings


class Student(Base):
    """Represents a student entity."""

    __tablename__ = "student"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    course_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('course.id'), nullable=False)
    attendance_id: Mapped[String] = mapped_column(String, nullable=False)

    course_activity_records = relationship(
        "CourseStudentActivityRecord",
        backref=backref("student")
    )
