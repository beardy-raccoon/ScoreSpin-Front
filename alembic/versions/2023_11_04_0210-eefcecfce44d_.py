"""empty message

Revision ID: eefcecfce44d
Revises: 
Create Date: 2023-11-04 02:10:10.677025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eefcecfce44d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tournaments',
    sa.Column('tournament_type', sa.Enum('standard', 'extend', native_enum=False), nullable=False),
    sa.Column('tournament_date', sa.Date(), nullable=False),
    sa.Column('tournament_coefficient', sa.Float(), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('user_role', sa.Enum('admin', 'moderator', 'user', native_enum=False), server_default=sa.text('user'), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('games',
    sa.Column('winner_player_id', sa.Uuid(), nullable=False),
    sa.Column('looser_player_id', sa.Uuid(), nullable=False),
    sa.Column('winner_score', sa.Integer(), nullable=False),
    sa.Column('looser_score', sa.Integer(), nullable=False),
    sa.Column('tournament_pid', sa.Integer(), nullable=True),
    sa.Column('game_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.ForeignKeyConstraint(['looser_player_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['tournament_pid'], ['tournaments.pid'], ),
    sa.ForeignKeyConstraint(['winner_player_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('base', sa.String(), nullable=True),
    sa.Column('left_side', sa.String(), nullable=True),
    sa.Column('right_side', sa.String(), nullable=True),
    sa.Column('game_style', sa.Boolean(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    op.create_table('players_tournaments_m2m',
    sa.Column('profile_pid', sa.Integer(), nullable=False),
    sa.Column('tournament_pid', sa.Integer(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.ForeignKeyConstraint(['profile_pid'], ['profiles.pid'], ),
    sa.ForeignKeyConstraint(['tournament_pid'], ['tournaments.pid'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('profile_pid', 'tournament_pid', name='unique_prof_tour')
    )
    op.create_table('ratings',
    sa.Column('profile_pid', sa.Integer(), nullable=False),
    sa.Column('rating_total', sa.Integer(), nullable=False),
    sa.Column('rating_diff', sa.Integer(), nullable=False),
    sa.Column('rating_registrations', sa.DateTime(), nullable=False),
    sa.Column('game_pid', sa.Integer(), nullable=False),
    sa.Column('tournament_pid', sa.Integer(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.ForeignKeyConstraint(['game_pid'], ['games.pid'], ),
    sa.ForeignKeyConstraint(['profile_pid'], ['profiles.pid'], ),
    sa.ForeignKeyConstraint(['tournament_pid'], ['tournaments.pid'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    op.drop_table('players_tournaments_m2m')
    op.drop_table('profiles')
    op.drop_table('games')
    op.drop_table('users')
    op.drop_table('tournaments')
    # ### end Alembic commands ###
