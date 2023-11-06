from typing import Annotated
from app.schemas.course import CourseCreate, Course
from app.db.dao.course import CourseDAO
from app.db.dao.user_course import UserCourseDao
from app.schemas.user_course import UserCourseCreate

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

from app.db.models.users import current_active_user, current_superuser
router = APIRouter()


@router.post("/")
async def create_course(
    course: Annotated[CourseCreate, Body(...)],
    dao: CourseDAO = Depends(),
    user_course_dao: UserCourseDao = Depends(),
    current_active_user = Depends(current_active_user),
) -> Course:
    """
    Creates an course.
    """

    course = Course.from_orm(await dao.create(course))
    await user_course_dao.create(
        UserCourseCreate(
            user_email=current_active_user.email,
            course_id=course.id,
            role="admin")
        )

    return course


@router.get("/")
async def get_all_courses(
    dao: UserCourseDao = Depends(),
    limit: int = 100,
    offset: int = 0,
    current_active_user = Depends(current_active_user),
) -> list[Course]:
    """
    Gets all courses.
    """
    return await dao.get_all_courses_for_user(user=current_active_user, limit=limit, offset=offset)
