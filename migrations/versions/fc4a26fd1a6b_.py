"""empty message

Revision ID: fc4a26fd1a6b
Revises: 
Create Date: 2019-02-27 01:42:36.940779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc4a26fd1a6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('appointment_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('patient_card_number', sa.String(length=250), nullable=False),
    sa.Column('doctor_permit_number', sa.String(length=250), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('slots', sa.JSON(), nullable=False),
    sa.Column('appointment_type', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    op.create_table('doctor',
    sa.Column('permit_number', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('first_name', sa.String(length=250), nullable=False),
    sa.Column('speciality', sa.String(length=250), nullable=False),
    sa.Column('city', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('permit_number')
    )
    op.create_table('nurse',
    sa.Column('access_id', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('access_id')
    )
    op.create_table('patient',
    sa.Column('card_number', sa.String(length=250), nullable=False),
    sa.Column('birth_day', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('phone_number', sa.String(length=250), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('card_number')
    )
    op.create_table('availability',
    sa.Column('availability_id', sa.Integer(), nullable=False),
    sa.Column('doctor_permit_number', sa.String(length=250), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('slots', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_permit_number'], ['doctor.permit_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('availability_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('availability')
    op.drop_table('patient')
    op.drop_table('nurse')
    op.drop_table('doctor')
    op.drop_table('appointment')
    # ### end Alembic commands ###
