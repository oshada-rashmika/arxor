"""create spatial gist index on experiences location

Revision ID: 09b9b986656f
Revises: 332a238816b4
Create Date: 2026-10-03 19:19:33.426419

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "09b9b986656f"
down_revision: Union[str, Sequence[str], None] = "332a238816b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Remove existing spatial index if present to avoid duplicate spatial indexes
    op.execute("DROP INDEX IF EXISTS idx_experiences_location")
    op.create_index(
        "ix_experiences_location_gist",
        "experiences",
        ["location"],
        unique=False,
        postgresql_using="gist",
    )


def downgrade() -> None:
    op.drop_index(
        "ix_experiences_location_gist",
        table_name="experiences",
        postgresql_using="gist",
    )
