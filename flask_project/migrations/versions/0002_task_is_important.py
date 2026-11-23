"""Додано ознаку важливого завдання."""
from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("task", sa.Column("is_important", sa.Boolean(), nullable=False, server_default=sa.text("0")))


def downgrade():
    with op.batch_alter_table("task") as batch_op:
        batch_op.drop_column("is_important")
