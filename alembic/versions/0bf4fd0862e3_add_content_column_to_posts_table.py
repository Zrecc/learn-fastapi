"""add content column to posts table

Revision ID: 0bf4fd0862e3
Revises: 373d4d5cab4d
Create Date: 2023-01-26 14:03:17.358605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf4fd0862e3'
down_revision = '373d4d5cab4d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
