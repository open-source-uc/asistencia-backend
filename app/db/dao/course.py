from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import Course
from app.schemas.course import CourseCreate


class CourseDAO:
    """Class for accessing course data."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, record: Course):
        """
        Creates a course.

        :param record: course to create.
        """
        instance = Course(**record.dict())

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Course]:
        """
        Get all courses with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(Course).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def filter(
        self,
        course_id: Optional[str] = None,
    ) -> List[Course]:
        """
        Get specific course.

        :param course_id: id of course instance.
        :return: course.
        """
        query = select(Course)
        if course_id:
            query = query.where(Course.id == course_id)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
