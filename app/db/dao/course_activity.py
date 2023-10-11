from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import CourseActivity
from app.schemas.course_activity import CourseActivityCreate

class CourseActivityDAO:
    """Class for accessing CourseActivity data."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, record: CourseActivity):
        """
            Creates a CourseActivity.

            :param record: CourseActivity to create.
        """
        instance = CourseActivity(**record.dict())

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[CourseActivity]:
        """
        Get all CourseActivities with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(CourseActivity).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def get_all_activities_on_course(self, course_id: str, limit: int = 100, offset: int = 0) -> List[CourseActivity]:
        """
        Get all CourseActivities with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(CourseActivity).where(CourseActivity.course_id == course_id).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def filter(
        self,
        course_activity_id: Optional[str] = None,
    ) -> List[CourseActivity]:
        """
        Get specific CourseActivity.

        :param CourseActivity_id: id of CourseActivity instance.
        :return: CourseActivity.
        """
        query = select(CourseActivity)
        if course_activity_id:
            query = query.where(CourseActivity.id == course_activity_id)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
