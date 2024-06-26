"""create table

Revision ID: 74964f114163
Revises: 572f12f2e3d3
Create Date: 2024-05-10 11:05:04.866096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74964f114163'
down_revision: Union[str, None] = '572f12f2e3d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lang', sa.String(length=2), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'lang')
    # ### end Alembic commands ###
