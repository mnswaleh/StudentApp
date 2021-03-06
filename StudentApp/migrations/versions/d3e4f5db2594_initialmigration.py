"""InitialMigration

Revision ID: d3e4f5db2594
Revises: 
Create Date: 2021-07-16 04:47:53.210504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3e4f5db2594'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('StudentNo', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('StudentNo')
    )
    op.create_table('certificate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('applicant', sa.Integer(), nullable=False),
    sa.Column('course', sa.Integer(), nullable=False),
    sa.Column('applicationDate', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('recieved', sa.Boolean(), server_default='false', nullable=False),
    sa.ForeignKeyConstraint(['applicant'], ['student.id'], ),
    sa.ForeignKeyConstraint(['course'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificate')
    op.drop_table('student')
    op.drop_table('course')
    # ### end Alembic commands ###
