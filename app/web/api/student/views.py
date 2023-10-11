from typing import Annotated
from app.schemas.student import StudentCreate, Student
from app.db.dao.student import StudentDAO

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

router = APIRouter()

@router.post("/")
async def create_student(
    course_id: str,
    student: Annotated[StudentCreate, Body(...)],
    dao: StudentDAO = Depends()
) -> Student:
    """
    Creates an student.
    """

    student.course_id = course_id
    return Student.from_orm(await dao.create(student))

@router.get("/")
async def get_all_students(
    course_id: str,
    dao: StudentDAO = Depends(),
    limit: int = 100,
    offset: int = 0,
):
    """
    Gets all students.
    """
    return await dao.get_all_students_on_course(course_id, limit, offset)