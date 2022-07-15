"""empty message

Revision ID: c4152d271d57
Revises: a6ab2a579b5e
Create Date: 2022-07-15 09:34:00.560621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4152d271d57'
down_revision = 'a6ab2a579b5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projects_stocks_id_fkey', 'projects', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('projects_stocks_id_fkey', 'projects', 'stock_list', ['stocks_id'], ['id'])
    # ### end Alembic commands ###
