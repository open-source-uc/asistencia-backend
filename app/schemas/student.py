from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, HttpUrl, UUID4


class StudentBase(BaseModel):
    """Represents a student entity."""

    course_id: Optional[str] = None
    attendance_codes: Optional[List[str]] = None


class StudentCreate(StudentBase):
    """Represents a student entity."""
    attendance_codes: List[str]

class StudentSearch(BaseModel):
    attendance_id: Optional[str] = None
    attendance_codes: Optional[List[str]] = None

class Student(StudentCreate):
    id: Optional[UUID4] = None

    class Config:
        from_attributes = True
