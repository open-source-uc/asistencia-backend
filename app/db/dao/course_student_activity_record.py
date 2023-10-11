from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import CourseStudentActivityRecord, CourseActivity, Student
from app.schemas.course_student_activity_record import CourseStudentActivityRecordCreate

class CourseStudentActivityRecordDAO:
    """Class for accessing course student activity record data."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, record: CourseStudentActivityRecordCreate, course_id: str, activity_slug: str):
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        course_activity = (await self.session.execute(
            select(CourseActivity).where(
                CourseActivity.slug == activity_slug and CourseActivity.course_id == course_id
            )
        )).scalar()

        student = (await self.session.execute(
            select(Student).where(
                Student.attendance_id == record.student_attendance_id and Student.course_id == course_id
            )
        )).scalar()

        if not course_activity or not student:
            raise Exception("Student or course activity not found")

        instance = CourseStudentActivityRecord(
                student_id=student.id,
                course_activity_id=course_activity.id,
            )

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all_records(self, limit: int = 100, offset: int = 0) -> List[CourseStudentActivityRecord]:
        """
        Get all course student activity records with limit/offset pagination.

        :param limit: limit of records.
        :param offset: offset of records.
        :return: stream of records.
        """
        raw_records = await self.session.execute(
            select(CourseStudentActivityRecord).limit(limit).offset(offset),
        )

        return list(raw_records.scalars().fetchall())

    async def filter(
        self,
        student_id: Optional[str] = None,
    ) -> List[CourseStudentActivityRecord]:
        """
        Get specific course student activity record.

        :param student_id: id of student instance.
        :return: course student activity records.
        """
        query = select(CourseStudentActivityRecord)
        if student_id:
            query = query.where(CourseStudentActivityRecord.student_id == student_id)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
