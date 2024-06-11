"""add contents row

Revision ID: 0655d23f4c2c
Revises: 070f6356d280
Create Date: 2024-06-11 13:58:26.412286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0655d23f4c2c'
down_revision: Union[str, None] = '070f6356d280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
