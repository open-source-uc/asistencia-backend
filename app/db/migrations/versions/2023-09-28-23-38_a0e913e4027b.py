"""Create courses table

Revision ID: a0e913e4027b
Revises: 1df1f70bcaa9
Create Date: 2023-09-28 23:38:38.596591

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = "a0e913e4027b"
down_revision = "1df1f70bcaa9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "course",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            server_default=sa.text("uuid_generate_v4()"),
            primary_key=True,
        ),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("semester", sa.String(length=10), nullable=False),
        sa.Column("section", sa.String(length=10), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("course")
