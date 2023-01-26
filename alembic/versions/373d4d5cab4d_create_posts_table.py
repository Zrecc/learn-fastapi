"""create posts table

Revision ID: 373d4d5cab4d
Revises: 
Create Date: 2023-01-26 13:50:44.661781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '373d4d5cab4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, 
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
