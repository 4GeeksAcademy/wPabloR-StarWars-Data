"""empty message

Revision ID: 17b65d13b9bc
Revises: a5cffa318ac2
Create Date: 2025-07-05 10:42:26.501013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b65d13b9bc'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('signup_date', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=False))
        batch_op.drop_column('password')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')
        batch_op.drop_column('signup_date')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
