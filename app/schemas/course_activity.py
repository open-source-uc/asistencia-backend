from typing import Optional, List, Union
from datetime import datetime

from pydantic import BaseModel, HttpUrl, UUID4


class CourseActivityBase(BaseModel):
    """Represents a CourseActivity entity."""

    slug: str
    date: datetime
    event_type: Optional[int] = 1
    course_id: Optional[str] = None


class CourseActivityCreate(CourseActivityBase):
    """Represents a CourseActivity entity."""

    pass


class CourseActivity(CourseActivityBase):
    id: Optional[UUID4] = None

    class Config:
        from_attributes = True
