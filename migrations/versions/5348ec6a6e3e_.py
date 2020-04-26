"""empty message

Revision ID: 5348ec6a6e3e
Revises: 7a6f073df1c0
Create Date: 2020-04-24 13:48:36.101314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5348ec6a6e3e'
down_revision = '7a6f073df1c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('training_job', sa.Column('minutes_trained', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('training_job', 'minutes_trained')
    # ### end Alembic commands ###