"""Exceptions Table

Revision ID: 6245d75fa12
Revises: e0a6af364a3f
Create Date: 2016-08-16 11:35:38.575026

"""

# revision identifiers, used by Alembic.
revision = '6245d75fa12'
down_revision = 'e0a6af364a3f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exceptions',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('source', sa.String(length=256), nullable=False),
                    sa.Column('occurred', sa.DateTime(), nullable=False),
                    sa.Column('ttl', sa.DateTime(), nullable=False),
                    sa.Column('type', sa.String(length=256), nullable=False),
                    sa.Column('message', sa.String(length=512), nullable=True),
                    sa.Column('stacktrace', sa.Text(), nullable=True),
                    sa.Column('region', sa.String(length=32), nullable=True),
                    sa.Column('tech_id', sa.Integer(), nullable=True),
                    sa.Column('item_id', sa.Integer(), nullable=True),
                    sa.Column('account_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
                    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
                    sa.ForeignKeyConstraint(['tech_id'], ['technology.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index('ix_exceptions_account_id', 'exceptions',
                    ['account_id'], unique=False)
    op.create_index('ix_exceptions_item_id', 'exceptions',
                    ['item_id'], unique=False)
    op.create_index('ix_exceptions_region', 'exceptions',
                    ['region'], unique=False)
    op.create_index('ix_exceptions_source', 'exceptions',
                    ['source'], unique=False)
    op.create_index('ix_exceptions_tech_id', 'exceptions',
                    ['tech_id'], unique=False)
    op.create_index('ix_exceptions_type', 'exceptions', ['type'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_exceptions_type', table_name='exceptions')
    op.drop_index('ix_exceptions_tech_id', table_name='exceptions')
    op.drop_index('ix_exceptions_source', table_name='exceptions')
    op.drop_index('ix_exceptions_region', table_name='exceptions')
    op.drop_index('ix_exceptions_item_id', table_name='exceptions')
    op.drop_index('ix_exceptions_account_id', table_name='exceptions')
    op.drop_table('exceptions')
    ### end Alembic commands ###
