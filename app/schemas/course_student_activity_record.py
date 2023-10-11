from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, HttpUrl, UUID4

class CourseStudentActivityRecordBase(BaseModel):
    """Represents a CourseStudentActivityRecord entity."""
    student_id: Optional[UUID4] = None
    course_activity_id: Optional[UUID4] = None

class CourseStudentActivityRecordCreate(BaseModel):
    """Represents a CourseStudentActivityRecord entity."""
    student_attendance_id: str

class CourseStudentActivityRecord(CourseStudentActivityRecordBase):
    id: Optional[UUID4] = None

    class Config:
        from_attributes = True
