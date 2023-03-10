"""retirement added

Revision ID: bec97a6a8117
Revises: eee03413b9d8
Create Date: 2022-07-18 10:01:14.007101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bec97a6a8117'
down_revision = 'eee03413b9d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('retirement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_age', sa.Integer(), nullable=True),
    sa.Column('age_at_retirement', sa.Integer(), nullable=True),
    sa.Column('years_to_payout', sa.Integer(), nullable=True),
    sa.Column('returns_during_accumulation', sa.Float(), nullable=True),
    sa.Column('returns_after_retirement', sa.Float(), nullable=True),
    sa.Column('annual_inflation_rate', sa.Float(), nullable=True),
    sa.Column('current_annual_salary', sa.Float(), nullable=True),
    sa.Column('annual_increase_in_salary', sa.Float(), nullable=True),
    sa.Column('percentage_of_salary_contributed', sa.Float(), nullable=True),
    sa.Column('salary_during_retirement', sa.Float(), nullable=True),
    sa.Column('current_retirement_saving_balance', sa.Float(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('retirement')
    # ### end Alembic commands ###
