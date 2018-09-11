"""adjusting to heroku errord

Revision ID: 9417beb3fb45
Revises: 4c8b6ec1981a
Create Date: 2018-09-11 16:26:51.057370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9417beb3fb45'
down_revision = '4c8b6ec1981a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###