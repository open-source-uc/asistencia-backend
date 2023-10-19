from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.db.dao.course_student_activity_record import CourseStudentActivityRecordDAO

router = APIRouter()


class SpreadsheetsPayload(BaseModel):
    course_id: str
    students_ids: list[str]
    activities_slugs: list[str]


@router.post("/check_assistance")
async def check_assistance(
    payload: SpreadsheetsPayload, dao: CourseStudentActivityRecordDAO = Depends()
):
    """
    Checks the assistance given a user_id rows
    and activity_slug columns.
    """

    activity_matrix = await dao.get_activity_matrix(
        activities=payload.activities_slugs,
        students_attendance_ids=payload.students_ids,
        course_id=payload.course_id,
    )

    return activity_matrix
