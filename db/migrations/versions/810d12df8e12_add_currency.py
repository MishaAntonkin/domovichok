"""add currency

Revision ID: 810d12df8e12
Revises: 6ca1777ef8cf
Create Date: 2018-04-18 16:58:31.950813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '810d12df8e12'
down_revision = '6ca1777ef8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flat', sa.Column('currency', sa.String(length=3), nullable=True))
    op.create_index(op.f('ix_flat_currency'), 'flat', ['currency'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_flat_currency'), table_name='flat')
    op.drop_column('flat', 'currency')
    # ### end Alembic commands ###
