"""create bookings table

Revision ID: 53e40bb8fbcc
Revises: 09b9b986656f
Create Date: 2026-10-03 19:35:06.205729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '53e40bb8fbcc'
down_revision: Union[str, Sequence[str], None] = '09b9b986656f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    booking_status_enum = postgresql.ENUM(
        'pending',
        'confirmed',
        'cancelled',
        'completed',
        name='booking_status',
    )
    booking_status_enum.create(op.get_bind(), checkfirst=True)

    payment_status_enum = postgresql.ENUM(
        'unpaid',
        'pending',
        'paid',
        'failed',
        'refunded',
        name='payment_status',
    )
    payment_status_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        'bookings',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('experience_id', sa.UUID(), nullable=False),
        sa.Column('customer_id', sa.UUID(), nullable=False),
        sa.Column(
            'status',
            postgresql.ENUM(
                'pending',
                'confirmed',
                'cancelled',
                'completed',
                name='booking_status',
                create_type=False,
            ),
            server_default='pending',
            nullable=False,
        ),
        sa.Column('slot_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            'total_price',
            sa.Numeric(precision=10, scale=2),
            server_default='0',
            nullable=False,
        ),
        sa.Column(
            'payment_status',
            postgresql.ENUM(
                'unpaid',
                'pending',
                'paid',
                'failed',
                'refunded',
                name='payment_status',
                create_type=False,
            ),
            server_default='unpaid',
            nullable=False,
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
    op.create_index(
        op.f('ix_bookings_customer_id'),
        'bookings',
        ['customer_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_bookings_experience_id'),
        'bookings',
        ['experience_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_bookings_slot_time'),
        'bookings',
        ['slot_time'],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f('ix_bookings_slot_time'), table_name='bookings')
    op.drop_index(op.f('ix_bookings_experience_id'), table_name='bookings')
    op.drop_index(op.f('ix_bookings_customer_id'), table_name='bookings')
    op.drop_table('bookings')
    op.execute('DROP TYPE IF EXISTS payment_status')
    op.execute('DROP TYPE IF EXISTS booking_status')
