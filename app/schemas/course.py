from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, HttpUrl, UUID4

class CourseBase(BaseModel):
    """Represents a course entity."""
    name: str
    code: str
    year: int
    semester: str
    section: str
    enabled: bool

class CourseCreate(CourseBase):
    """Represents a course entity."""
    pass

class Course(CourseBase):
    id: Optional[UUID4] = None

    class Config:
        from_attributes = True

