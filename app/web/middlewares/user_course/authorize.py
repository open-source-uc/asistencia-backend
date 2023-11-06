from fastapi import Depends, HTTPException, status
from app.db.dao.user_course import UserCourseDao
from app.db.models.users import current_active_user

class UserCourseMiddleware:
    def __init__(self, allowed_roles: list[str] = ["admin", "assistant", "default"]):
        self.allowed_roles = allowed_roles

    async def __call__(self, course_id: str, user_course_dao: UserCourseDao = Depends(), current_active_user = Depends(current_active_user)):
        if not await user_course_dao.authorize_mail_for_course(course_id, current_active_user.email, self.allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is not authorized to perform this action.",
            )

        return current_active_user
