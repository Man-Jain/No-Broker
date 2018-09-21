"""empty message

Revision ID: a4809e8135e5
Revises: 
Create Date: 2018-09-21 09:53:44.800781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4809e8135e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('user_type', sa.String(length=1), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('properties',
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.Column('property_name', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('rent', sa.Integer(), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('landlord', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['landlord'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('property_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###