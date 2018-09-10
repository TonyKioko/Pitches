"""table alter after heroku fail

Revision ID: 4c8b6ec1981a
Revises: 11a19fc81c60
Create Date: 2018-09-10 22:37:30.859091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c8b6ec1981a'
down_revision = '11a19fc81c60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.add_column('pitches', sa.Column('published', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'published')
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
