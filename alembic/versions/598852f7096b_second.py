"""second

Revision ID: 598852f7096b
Revises: 8e15d495000e
Create Date: 2022-04-19 16:18:55.148403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598852f7096b'
down_revision = '8e15d495000e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('store_id', sa.Integer(), nullable=True))
    op.drop_constraint('products_store_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'store', ['store_id'], ['id'])
    op.drop_column('products', 'store')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('store', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_store_fkey', 'products', 'store', ['store'], ['id'])
    op.drop_column('products', 'store_id')
    # ### end Alembic commands ###
