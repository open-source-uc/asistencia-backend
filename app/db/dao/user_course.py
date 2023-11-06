from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import UserCourse
from app.schemas.user_course import UserCourseCreate


class UserCourseDao:
    """Manages CRUD operations for UserCourse entities."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, user_course_create: UserCourseCreate):
        """
        Creates a user_course.

        :param record: user_course to create.
        """
        instance = UserCourse(**user_course_create.dict())
        print(instance)

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[UserCourse]:
        """
        Get all UserCourse with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(UserCourse).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def get_all_user_for_course(
        self, course_id: str, limit: int = 100, offset: int = 0
    ) -> List[UserCourse]:
        """
        Get all UserCourse with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(UserCourse)
            .where(UserCourse.course_id == course_id)
            .limit(limit)
            .offset(offset),
        )

        return list(raw_records.scalars().fetchall())
