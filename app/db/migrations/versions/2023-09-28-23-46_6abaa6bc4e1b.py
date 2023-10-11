"""Create table CourseStudentActivityRecord

Revision ID: 6abaa6bc4e1b
Revises: 04381a3a1114
Create Date: 2023-09-28 23:46:10.276661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6abaa6bc4e1b"
down_revision = "04381a3a1114"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "course_student_activity_record",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            server_default=sa.text("uuid_generate_v4()"),
            primary_key=True,
        ),
        sa.Column("course_activity_id", sa.UUID(), nullable=False),
        sa.Column("student_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_activity_id"],
            ["course_activity.id"],
        ),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["student.id"],
        ),
    )

    op.create_index(
        op.f("ix_course_student_activity_record_course_activity_id"),
        "course_student_activity_record",
        ["course_activity_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_course_student_activity_record_student_id"),
        "course_student_activity_record",
        ["student_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_table("course_student_activity_record")
    op.drop_index(
        op.f("ix_course_student_activity_record_course_activity_id"),
        table_name="course_student_activity_record",
    )
    op.drop_index(
        op.f("ix_course_student_activity_record_student_id"),
        table_name="course_student_activity_record",
    )
