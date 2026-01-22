"""initial schema: users + balances

Revision ID: d20c7d752fdf
Revises: 
Create Date: 2026-01-21 18:13:17.440948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime
from zoneinfo import ZoneInfo


# revision identifiers, used by Alembic.
revision: str = 'd20c7d752fdf'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),  # or sa.Enum if using Enum
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    # Create balances table
    op.create_table(
        'balances',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('coin', sa.String(length=10), nullable=False),
        sa.Column('amount', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'coin', name='uq_user_coin')
    )


def downgrade() -> None:
    op.drop_table('balances')
    op.drop_table('users')
