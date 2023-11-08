from typing import Annotated
from app.schemas.student import StudentCreate, Student
from app.db.dao.student import StudentDAO

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from app.web.middlewares.user_course import UserCourseMiddleware

router = APIRouter()

@router.post("/")
async def create_student(
    course_id: str,
    student: Annotated[StudentCreate, Body(...)],
    dao: StudentDAO = Depends(),
    current_active_user = Depends(UserCourseMiddleware())
) -> Student:
    """
    Creates an student.
    """

    student.course_id = course_id
    return Student.from_orm(await dao.create(student))


@router.get("/")
async def get_all_students(
    course_id: str,
    limit: int = 100,
    offset: int = 0,
    dao: StudentDAO = Depends(),
    current_active_user = Depends(UserCourseMiddleware()),
):
    """
    Gets all students.
    """
    return await dao.get_all_students_on_course(course_id, limit, offset)
