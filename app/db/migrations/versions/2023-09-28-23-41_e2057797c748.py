"""Create students table

Revision ID: e2057797c748
Revises: a0e913e4027b
Create Date: 2023-09-28 23:41:28.692422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e2057797c748"
down_revision = "a0e913e4027b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "student",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            server_default=sa.text("uuid_generate_v4()"),
            primary_key=True,
        ),
        sa.Column("course_id", sa.UUID(), nullable=False),
        sa.Column("attendance_id", sa.String(length=100), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("student")
