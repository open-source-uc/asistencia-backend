"""Create table course activity

Revision ID: 04381a3a1114
Revises: e2057797c748
Create Date: 2023-09-28 23:43:23.258861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04381a3a1114'
down_revision = 'e2057797c748'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('course_activity',
    sa.Column('id', sa.UUID(), nullable=False, server_default=sa.text('uuid_generate_v4()'), primary_key=True),
    sa.Column('event_type', sa.Integer(), nullable=False, server_default='0'),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('course_id', sa.UUID(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    )


def downgrade() -> None:
    op.drop_table('course_activity')
