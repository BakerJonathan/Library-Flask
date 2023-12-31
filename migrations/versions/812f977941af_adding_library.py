"""adding library

Revision ID: 812f977941af
Revises: fb7df4ff4260
Create Date: 2023-06-28 11:54:53.257170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812f977941af'
down_revision = 'fb7df4ff4260'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('book_title', sa.String(length=150), nullable=True),
    sa.Column('ISBN', sa.Numeric(precision=20, scale=0), nullable=True),
    sa.Column('author', sa.String(length=150), nullable=True),
    sa.Column('publisher', sa.String(length=150), nullable=True),
    sa.Column('book_length', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('cover_type', sa.String(length=70), nullable=True),
    sa.Column('rental_status', sa.String(length=100), nullable=True),
    sa.Column('renter', sa.String(length=150), nullable=True),
    sa.Column('language', sa.String(length=100), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
