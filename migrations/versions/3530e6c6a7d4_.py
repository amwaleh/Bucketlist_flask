"""empty message

Revision ID: 3530e6c6a7d4
Revises: 385aff62e30e
Create Date: 2015-12-18 17:21:27.821971

"""

# revision identifiers, used by Alembic.
revision = '3530e6c6a7d4'
down_revision = '385aff62e30e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucketitem', sa.Column('logged', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucketitem', 'logged')
    ### end Alembic commands ###
