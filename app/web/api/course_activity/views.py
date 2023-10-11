from typing import Annotated
from app.schemas.course_activity import CourseActivityCreate, CourseActivity
from app.db.dao.course_activity import CourseActivityDAO

from fastapi import APIRouter, Body
from fastapi.param_functions import Depends

router = APIRouter()


@router.post("/")
async def create_course_activity(
    course_id: str,
    course_activity: Annotated[CourseActivityCreate, Body(...)],
    dao: CourseActivityDAO = Depends(),
) -> CourseActivity:
    """
    Creates an course_activity.
    """

    course_activity.course_id = course_id
    return CourseActivity.from_orm(await dao.create(course_activity))


@router.get("/")
async def get_all_course_activities(
    course_id: str,
    dao: CourseActivityDAO = Depends(),
    limit: int = 100,
    offset: int = 0,
):
    """
    Gets all course_activities.
    """
    return await dao.get_all_activities_on_course(course_id, limit, offset)
