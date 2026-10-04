"""create business_profiles table

Revision ID: d1ded28d6590
Revises: dcf6eb28a902
Create Date: 2026-10-03 13:36:15.564030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1ded28d6590"
down_revision: Union[str, Sequence[str], None] = "dcf6eb28a902"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "business_profiles",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("business_name", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("tier", sa.String(), server_default="free", nullable=False),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column(
            "is_verified",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        sa.Column("lankaqr_code", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("lankaqr_code"),
    )


def downgrade() -> None:
    op.drop_table("business_profiles")
