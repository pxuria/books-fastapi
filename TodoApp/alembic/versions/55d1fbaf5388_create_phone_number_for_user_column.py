"""Create Phone number for user column

Revision ID: 55d1fbaf5388
Revises: 38a1a484f994
Create Date: 2025-12-06 14:52:22.736452

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55d1fbaf5388'
down_revision: Union[str, Sequence[str], None] = '38a1a484f994'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
