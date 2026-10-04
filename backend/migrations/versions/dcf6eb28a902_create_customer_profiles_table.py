"""create customer_profiles table

Revision ID: dcf6eb28a902
Revises: 029793681162
Create Date: 2026-10-03 12:59:55.219092

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "dcf6eb28a902"
down_revision: Union[str, Sequence[str], None] = "029793681162"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "customer_profiles",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("avatar_url", sa.String(), nullable=True),
        sa.Column("tier", sa.String(), server_default="free", nullable=False),
        sa.Column("tier_expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("interests", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id"),
    )


def downgrade() -> None:
    op.drop_table("customer_profiles")
