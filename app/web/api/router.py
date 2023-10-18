from fastapi.routing import APIRouter

from app.web.api import (
    attendance,
    course,
    course_activity,
    docs,
    monitoring,
    spreadhsets,
    student,
    users,
)

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(docs.router)
api_router.include_router(spreadhsets.router)
api_router.include_router(course.router, prefix="/courses", tags=["course"])
api_router.include_router(
    student.router, prefix="/courses/{course_id}/students", tags=["student"]
)
api_router.include_router(
    course_activity.router, prefix="/courses/{course_id}/activities", tags=["activity"]
)
api_router.include_router(
    attendance.router,
    prefix="/courses/{course_id}/activities/{activity_slug}/attendances",
    tags=["attendance"],
)
