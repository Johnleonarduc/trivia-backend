"""empty message

Revision ID: d69a4fa9819a
Revises: 
Create Date: 2023-10-11 17:10:46.526435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69a4fa9819a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('difficulty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('categories')
    # ### end Alembic commands ###