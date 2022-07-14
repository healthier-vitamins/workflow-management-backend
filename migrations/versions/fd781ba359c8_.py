"""empty message

Revision ID: fd781ba359c8
Revises: 029545daf8cc
Create Date: 2022-07-14 23:41:09.433123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd781ba359c8'
down_revision = '029545daf8cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_accounts', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_accounts', type_='unique')
    # ### end Alembic commands ###
