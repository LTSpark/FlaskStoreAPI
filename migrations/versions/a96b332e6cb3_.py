"""empty message

Revision ID: a96b332e6cb3
Revises: 
Create Date: 2021-03-18 19:17:39.801073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a96b332e6cb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('users')  
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('units', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='products_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('birth_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    # ### end Alembic commands ###
