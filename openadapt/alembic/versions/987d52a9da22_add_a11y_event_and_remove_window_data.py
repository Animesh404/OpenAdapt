"""add_a11y_event_and_remove_window_data

Revision ID: 987d52a9da22
Revises: bb25e889ad71
Create Date: 2024-07-19 03:19:53.437136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987d52a9da22'
down_revision = 'bb25e889ad71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('a11y_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['handle'], ['window_event.handle'], name=op.f('fk_a11y_event_handle_window_event')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_a11y_event'))
    )
    with op.batch_alter_table('window_event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('handle', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('meta', sa.JSON(), nullable=True))
        batch_op.drop_column('window_id')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('window_event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('window_id', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('meta')
        batch_op.drop_column('handle')

    op.drop_table('a11y_event')
    # ### end Alembic commands ###