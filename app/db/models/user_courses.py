# type: ignore
import uuid

from fastapi import Depends
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Boolean, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.dialects.postgresql import ARRAY, ENUM

from app.db.base import Base
from app.db.dependencies import get_db_session
from app.settings import settings


class UserCourse(Base):
    """Represents a UserCourse entity."""

    __tablename__ = "user_course"

    user_email: Mapped[Optional[str]] = mapped_column(
        String, nullable=True
    )
    course_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("course.id"), primary_key=True
    )
    role: Mapped[str] = mapped_column(
        ENUM('admin', 'assistant', 'default', name='role_enum'), nullable=False, default="default"
    )
    active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True
    )
