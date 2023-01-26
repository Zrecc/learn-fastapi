"""add last few columns to posts table

Revision ID: 8f1a8591ceaf
Revises: a9022cba74fc
Create Date: 2023-01-26 15:02:24.756802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1a8591ceaf'
down_revision = 'a9022cba74fc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
      'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
      'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
    ))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
