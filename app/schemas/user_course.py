from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, HttpUrl, UUID4


class UserCourseBase(BaseModel):
    """Represents a UserCourse entity."""

    user_email: Optional[str] = None
    course_id: Optional[UUID4] = None
    role: Optional[str] = None
    active: Optional[bool] = None


class UserCourseCreate(UserCourseBase):
    """Represents a UserCourse entity."""

    pass


class UserCourse(UserCourseBase):
    id: Optional[UUID4] = None

    class Config:
        from_attributes = True

