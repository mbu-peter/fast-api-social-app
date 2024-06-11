"""create posts table

Revision ID: 070f6356d280
Revises: 
Create Date: 2024-06-11 13:43:55.856735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '070f6356d280'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_table('posts')
    pass
