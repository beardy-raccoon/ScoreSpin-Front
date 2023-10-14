"""empty message

Revision ID: 624503a752d1
Revises: 
Create Date: 2023-09-22 18:58:17.806762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '624503a752d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('second_name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    op.create_table('games',
    sa.Column('first_player_id', sa.Uuid(), nullable=False),
    sa.Column('second_player_id', sa.Uuid(), nullable=False),
    sa.Column('winner_id', sa.Uuid(), nullable=False),
    sa.Column('first_pl_score', sa.Integer(), nullable=False),
    sa.Column('second_pl_score', sa.Integer(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.ForeignKeyConstraint(['first_player_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['second_player_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    op.drop_table('users')
    # ### end Alembic commands ###