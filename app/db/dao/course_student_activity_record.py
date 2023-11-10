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
                    Student.attendance_codes.any(record.student_attendance_id),
                    Student.course_id == course_id
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

    async def get_for_many(
        self, course_id: str, students_attendance_ids: List[str], activities: List[str]
    ):
        """
        Gets every assistance of each activity for each student in a course.
        :param course_id: The course id.
        :param students_attendance_ids: The list of students ids.
        :param activities: The list of activities slugs.
        """

        # TODO: falta manejar el hash

        # Ahora se asume que los students_attendance_ids ya está heasheado
        students_query = select(
            Student.id.label("student_id"),
            # TODO: Esto debería ser un arreglo
            Student.attendance_id.label("student_code"),
        ).where(
            Student.course_id == course_id,
            Student.attendance_id.in_(students_attendance_ids),
        )
        students_with = students_query.cte("students")

        activities_query = select(
            CourseActivity.id.label("activity_id"),
            CourseActivity.slug,
        ).where(
            CourseActivity.course_id == course_id,
            CourseActivity.slug.in_(activities),
        )
        activities_with = activities_query.cte("activities")

        assistance_query = (
            select(
                students_with.c.student_code.label("student_code"),
                activities_with.c.slug.label("activity_slug"),
                CourseStudentActivityRecord.id,
            )
            .join(
                CourseStudentActivityRecord,
                CourseStudentActivityRecord.student_id == students_with.c.student_id,
            )
            .join(
                CourseActivity,
                CourseActivity.id == CourseStudentActivityRecord.course_activity_id,
            )
        )
        assistance_with = assistance_query.cte("assistance_query")

        inner_agg_subquery = (
            select(
                assistance_with.c.student_code,
                func.json_object_agg(
                    assistance_with.c.activity_slug,
                    func.json_build_object("created_at", 0),
                ).label("activity_data"),
            )
            .group_by(assistance_with.c.student_code)
            .alias("inner_agg_subquery")
        )
        final_query = select(
            func.json_object_agg(
                inner_agg_subquery.c.student_code, inner_agg_subquery.c.activity_data
            )
        )

        result = await self.session.execute(final_query)
        mapping = result.scalars().first()

        return mapping
