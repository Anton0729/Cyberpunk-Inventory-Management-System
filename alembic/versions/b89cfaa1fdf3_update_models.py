"""Update models

Revision ID: b89cfaa1fdf3
Revises: 7d8089c86e53
Create Date: 2024-08-19 12:28:00.392828

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b89cfaa1fdf3"
down_revision: Union[str, None] = "7d8089c86e53"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_user_id", table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("hashed_password", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
        sa.UniqueConstraint("username", name="user_username_key"),
    )
    op.create_index("ix_user_id", "user", ["id"], unique=False)
    # ### end Alembic commands ###
