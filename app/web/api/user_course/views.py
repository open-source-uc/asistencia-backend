from typing import Annotated, List
from app.schemas.user_course import UserCourseCreate, UserCourse
from app.db.dao.user_course import UserCourseDao

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

router = APIRouter()


@router.post("/")
async def create(
    user_course: Annotated[UserCourseCreate, Body(...)],
    dao: UserCourseDao = Depends(),
) -> UserCourse:
    """Create a new user_course."""
    return UserCourse.from_orm(await dao.create(user_course))

@router.get("/")
async def get_all(
    dao: UserCourseDao = Depends(),
) -> List[UserCourse]:
    """Get all user_course."""
    return await dao.get_all()

@router.get("/{course_id}")
async def get_all_user_for_course(
    course_id: str,
    dao: UserCourseDao = Depends(),
) -> List[UserCourse]:
    """Get all user_course for a course."""
    return await dao.get_all_user_for_course(course_id)
