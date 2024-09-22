"""user alter table

Revision ID: 2dcd71a086ad
Revises: be2c9638461d
Create Date: 2024-09-22 17:33:59.162054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2dcd71a086ad'
down_revision: Union[str, None] = 'be2c9638461d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'password',
               existing_type=postgresql.BYTEA(),
               type_=sa.String(),
               existing_nullable=False)


def downgrade() -> None:
    op.alter_column('users', 'password',
               existing_type=sa.String(),
               type_=postgresql.BYTEA(),
               existing_nullable=False)
