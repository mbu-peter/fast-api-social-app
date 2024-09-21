"""migrate to neon

Revision ID: b74a3decafd4
Revises: af346a82f871
Create Date: 2024-09-21 12:35:32.091385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b74a3decafd4'
down_revision: Union[str, None] = 'af346a82f871'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
