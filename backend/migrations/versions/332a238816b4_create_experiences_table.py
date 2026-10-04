"""create experiences table

Revision ID: 332a238816b4
Revises: d1ded28d6590
Create Date: 2026-10-03 15:31:55.027512

"""
from typing import Sequence, Union

from alembic import op
import geoalchemy2
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "332a238816b4"
down_revision: Union[str, Sequence[str], None] = "d1ded28d6590"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "experiences",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("business_id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "location",
            geoalchemy2.types.Geometry(
                geometry_type="POINT",
                srid=4326,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                spatial_index=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "price",
            sa.Numeric(precision=10, scale=2),
            server_default="0",
            nullable=False,
        ),
        sa.Column("capacity", sa.Integer(), server_default="1", nullable=False),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["business_id"],
            ["business_profiles.user_id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "idx_experiences_location",
        "experiences",
        ["location"],
        unique=False,
        postgresql_using="gist",
    )


def downgrade() -> None:
    op.drop_index(
        "idx_experiences_location",
        table_name="experiences",
        postgresql_using="gist",
    )
    op.drop_table("experiences")
