"""create business_replies table

Revision ID: 6a4468704204
Revises: 617d57293449
Create Date: 2026-10-04 21:38:53.183386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a4468704204'
down_revision: Union[str, Sequence[str], None] = '617d57293449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'business_replies',
        sa.Column('review_id', sa.UUID(), nullable=False),
        sa.Column('business_id', sa.UUID(), nullable=False),
        sa.Column('reply_content', sa.Text(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ['business_id'],
            ['business_profiles.user_id'],
        ),
        sa.ForeignKeyConstraint(
            ['review_id'],
            ['reviews.id'],
        ),
        sa.PrimaryKeyConstraint('review_id'),
    )


def downgrade() -> None:
    op.drop_table('business_replies')
