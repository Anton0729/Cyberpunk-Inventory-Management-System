"""New migration

Revision ID: 839f2e0d8eb3
Revises: 0de044a3b4b7
Create Date: 2024-08-24 19:51:45.726863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '839f2e0d8eb3'
down_revision: Union[str, None] = '0de044a3b4b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
