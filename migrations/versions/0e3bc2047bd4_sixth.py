"""sixth

Revision ID: 0e3bc2047bd4
Revises: c736922a15fc
Create Date: 2022-07-04 23:13:15.467613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3bc2047bd4'
down_revision = 'c736922a15fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('f', sa.Text(), nullable=True))
    op.add_column('questionsmarks', sa.Column('f', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questionsmarks', 'f')
    op.drop_column('questions', 'f')
    # ### end Alembic commands ###