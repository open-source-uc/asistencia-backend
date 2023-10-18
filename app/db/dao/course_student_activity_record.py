from typing import List, Optional

from fastapi import Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db_session
from app.db.models import CourseActivity, CourseStudentActivityRecord, Student
from app.schemas.course_student_activity_record import CourseStudentActivityRecordCreate


class CourseStudentActivityRecordDAO:
    """Class for accessing course student activity record data."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
        self,
        record: CourseStudentActivityRecordCreate,
        course_id: str,
        activity_slug: str,
    ):
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        course_activity = (
            await self.session.execute(
                select(CourseActivity).where(
                    CourseActivity.slug == activity_slug
                    and CourseActivity.course_id == course_id
                )
            )
        ).scalar()

        student = (
            await self.session.execute(
                select(Student).where(
                    Student.attendance_id == record.student_attendance_id
                    and Student.course_id == course_id
                )
            )
        ).scalar()

        if not course_activity or not student:
            raise Exception("Student or course activity not found")

        instance = CourseStudentActivityRecord(
            student_id=student.id,
            course_activity_id=course_activity.id,
        )

        self.session.add(instance)
        await self.session.commit()

        return instance

    async def get_all_records(
        self, limit: int = 100, offset: int = 0
    ) -> List[CourseStudentActivityRecord]:
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

    async def get_activity_matrix(
        self, course_id: str, students_attendance_ids: List[str], activities: List[str]
    ):
        """
        Get the [student] x [activity] matrix.
        The returned array should be a list of lists, where each list
        represents a student and each element in the list represents an activity.
        """
        # TODO: match with hashed ids
        # TODO: add something to allow matching the order of the students (return back the attendances ids?)
        # TODO: fix bug where it fills the matrix with the same value
        query = (
            select(
                Student.id,
                func.json_object_agg(
                    CourseActivity.slug,
                    func.coalesce(CourseStudentActivityRecord.id, None),
                ).label("activities"),
            )
            .join(
                CourseStudentActivityRecord,
                Student.id == CourseStudentActivityRecord.student_id,
            )
            .join(
                CourseActivity,
                CourseActivity.course_id == Student.course_id,
            )
            .where(
                Student.course_id == course_id,
                CourseActivity.slug.in_(activities),
                Student.attendance_id.in_(students_attendance_ids),
            )
            .group_by(
                Student.id,
            )
        )

        rows = await self.session.execute(query)
        return {k: v for k, v in rows.fetchall()}
