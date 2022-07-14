"""empty message

Revision ID: a6ab2a579b5e
Revises: fd781ba359c8
Create Date: 2022-07-15 01:53:43.771252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6ab2a579b5e'
down_revision = 'fd781ba359c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stocks_id', sa.Integer(), nullable=True),
    sa.Column('services_required', sa.String(length=50), nullable=True),
    sa.Column('customer_company', sa.String(length=50), nullable=True),
    sa.Column('customer_poc_name', sa.String(length=50), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stocks_id'], ['stock_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_timestamp'), 'projects', ['timestamp'], unique=False)
    op.add_column('stock_list', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stock_list', 'quantity')
    op.drop_index(op.f('ix_projects_timestamp'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###