from typing import Annotated
from app.schemas.course import CourseCreate, Course
from app.db.dao.course import CourseDAO

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

router = APIRouter()


@router.post("/")
async def create_course(
    course: Annotated[CourseCreate, Body(...)], dao: CourseDAO = Depends()
) -> Course:
    """
    Creates an course.
    """

    return Course.from_orm(await dao.create(course))


@router.get("/")
async def get_all_courses(
    dao: CourseDAO = Depends(),
    limit: int = 100,
    offset: int = 0,
) -> list[Course]:
    """
    Gets all courses.
    """
    return await dao.get_all(limit, offset)
