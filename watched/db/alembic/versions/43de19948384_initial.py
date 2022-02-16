"""Initial

Revision ID: 43de19948384
Revises: 
Create Date: 2022-02-16 12:07:21.698480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43de19948384'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watch_history',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('is_show', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__watch_history'))
    )
    op.create_index('ix__user_id_datetime', 'watch_history', ['user_id', 'datetime'], unique=False)
    op.create_table('watch_history_shows',
    sa.Column('watch_event_id', sa.Integer(), nullable=False),
    sa.Column('first_episode', sa.SmallInteger(), nullable=False),
    sa.Column('last_episode', sa.SmallInteger(), nullable=False),
    sa.Column('season', sa.SmallInteger(), nullable=True),
    sa.Column('finished_season', sa.Boolean(), nullable=True),
    sa.Column('finished_show', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['watch_event_id'], ['watch_history.id'], name=op.f('fk__watch_history_shows__watch_event_id__watch_history'), ondelete='CASCADE'),
    sa.UniqueConstraint('watch_event_id', name=op.f('uq__watch_history_shows__watch_event_id'))
    )
    op.create_table('watched',
    sa.Column('watch_event_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.SmallInteger(), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['watch_event_id'], ['watch_history.id'], name=op.f('fk__watched__watch_event_id__watch_history'), ondelete='CASCADE'),
    sa.UniqueConstraint('watch_event_id', name=op.f('uq__watched__watch_event_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watched')
    op.drop_table('watch_history_shows')
    op.drop_index('ix__user_id_datetime', table_name='watch_history')
    op.drop_table('watch_history')
    # ### end Alembic commands ###
