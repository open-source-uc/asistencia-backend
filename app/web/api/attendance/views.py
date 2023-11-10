from typing import Annotated
from app.schemas.course_student_activity_record import (
    CourseStudentActivityRecordCreate,
    CourseStudentActivityRecord,
)
from app.db.dao.course_student_activity_record import CourseStudentActivityRecordDAO
from app.web.middlewares.user_course import UserCourseMiddleware

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

router = APIRouter()


@router.post("/")
async def create_attendance_record(
    course_id: str,
    activity_slug: str,
    attendance_record: Annotated[CourseStudentActivityRecordCreate, Body(...)],
    dao: CourseStudentActivityRecordDAO = Depends(),
    current_active_user = Depends(UserCourseMiddleware()),
):
    """
    Creates an attendance record for a student in a course activity.
    """

    return CourseStudentActivityRecord.from_orm(
        await dao.create(attendance_record, course_id, activity_slug)
    )


@router.get("/")
async def get_attendance_records(dao: CourseStudentActivityRecordDAO = Depends(), current_active_user = Depends(UserCourseMiddleware())):
    """
    Gets all attendance records.
    """
    return await dao.get_all_records(100, 0)
