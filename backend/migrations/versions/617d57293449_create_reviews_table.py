"""create reviews table

Revision ID: 617d57293449
Revises: 53e40bb8fbcc
Create Date: 2026-10-04 09:09:13.226997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '617d57293449'
down_revision: Union[str, Sequence[str], None] = '53e40bb8fbcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'reviews',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('experience_id', sa.UUID(), nullable=False),
        sa.Column('customer_id', sa.UUID(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('authenticity_rating', sa.Integer(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.CheckConstraint(
            'rating >= 1 AND rating <= 5',
            name='ck_reviews_rating_range',
        ),
        sa.CheckConstraint(
            'authenticity_rating >= 1 AND authenticity_rating <= 5',
            name='ck_reviews_authenticity_rating_range',
        ),
        sa.ForeignKeyConstraint(
            ['customer_id'],
            ['customer_profiles.user_id'],
        ),
        sa.ForeignKeyConstraint(
            ['experience_id'],
            ['experiences.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('reviews')
