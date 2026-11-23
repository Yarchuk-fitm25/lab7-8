"""Початкові таблиці планувальника."""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("course",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("code", sa.String(length=15), nullable=False, unique=True),
        sa.Column("semester", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
    )
    op.create_table("label",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=40), nullable=False, unique=True),
        sa.Column("color", sa.String(length=10), nullable=False),
        sa.Column("description", sa.String(length=150), nullable=False),
    )
    op.create_table("task",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(length=20), nullable=False, unique=True),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("due_date", sa.Date(), nullable=False),
        sa.Column("priority", sa.String(length=10), nullable=False),
        sa.Column("status", sa.String(length=10), nullable=False),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("course.id", ondelete="RESTRICT"), nullable=False),
    )
    op.create_table("task_plan",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task_id", sa.Integer(), sa.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("steps", sa.Text(), nullable=False),
        sa.Column("planned_hours", sa.Integer(), nullable=False),
        sa.Column("resource_url", sa.String(length=250), nullable=False),
        sa.Column("notes", sa.Text(), nullable=False),
    )
    op.create_table("task_labels",
        sa.Column("task_id", sa.Integer(), sa.ForeignKey("task.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("label_id", sa.Integer(), sa.ForeignKey("label.id", ondelete="CASCADE"), primary_key=True),
    )


def downgrade():
    op.drop_table("task_labels")
    op.drop_table("task_plan")
    op.drop_table("task")
    op.drop_table("label")
    op.drop_table("course")
