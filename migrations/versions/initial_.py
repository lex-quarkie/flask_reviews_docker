from datetime import datetime

from alembic import op
import sqlalchemy as sa

revision = "initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('products',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.String(length=255), autoincrement=False, nullable=False),
                    sa.Column('asin', sa.String(length=255), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='products_pkey'),
                    )
    op.create_table('reviews',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('product_asin', sa.String(length=255), nullable=False),
                    sa.Column('title', sa.String(length=255), autoincrement=False, nullable=False),
                    sa.Column('review_text', sa.String(length=255), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='reviews_pkey'),
                    )


def downgrade():
    op.drop_table("reviews")
    op.drop_table("products")
