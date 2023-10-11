from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import Student
from app.schemas.student import StudentCreate


class StudentDAO:
    """Class for accessing student data."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, student_create: StudentCreate):
        """
        Creates a student.

        :param record: student to create.
        """
        instance = Student(**student_create.dict())

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[Student]:
        """
        Get all Student with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(Student).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def get_all_students_on_course(
        self, course_id: str, limit: int = 100, offset: int = 0
    ) -> List[Student]:
        """
        Get all Student with limit/offset pagination.
        """

        raw_records = await self.session.execute(
            select(Student)
            .where(Student.course_id == course_id)
            .limit(limit)
            .offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def filter(
        self,
        student_id: Optional[str] = None,
    ) -> List[Student]:
        """
        Get specific student.

        :param student_id: id of student instance.
        :return: student.
        """
        query = select(Student)
        if student_id:
            query = query.where(student.id == student_id)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
