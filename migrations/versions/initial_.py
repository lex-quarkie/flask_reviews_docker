from alembic import op
import sqlalchemy as sa

revision = "initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
            sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
            sa.Column("title", sa.VARCHAR(length=5000), autoincrement=False),
            sa.Column("asin", sa.VARCHAR(length=500), autoincrement=False),
            sa.PrimaryKeyConstraint("id", name="products_pkey"),
            sa.UniqueConstraint("id"),
            sa.UniqueConstraint("asin"),
    )

    op.create_table(
        "reviews",
            sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
            sa.Column(
                "product_asin", sa.VARCHAR(length=500), autoincrement=False, nullable=False
            ),
            sa.Column("title", sa.VARCHAR(length=5000), autoincrement=False, nullable=False),
            sa.Column(
                "review_text", sa.VARCHAR(length=15000), autoincrement=False, nullable=False
            ),
            sa.ForeignKeyConstraint(
                ["product_asin"], ["products.asin"], name="reviews_product_asin_fkey"
            ),
            sa.PrimaryKeyConstraint("id", name="reviews_pkey"),
            sa.UniqueConstraint("id"),
    )


def downgrade():
    op.drop_table("reviews")
    op.drop_table("products")
