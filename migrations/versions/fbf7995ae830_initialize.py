"""initialize

Revision ID: fbf7995ae830
Revises: 
Create Date: 2023-07-09 16:14:09.131918

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table

# revision identifiers, used by Alembic.
revision = 'fbf7995ae830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dish_ingredient',
        Column('dish_id', Integer, ForeignKey('dishes.id')),
        Column('ingredient_id', Integer, ForeignKey('ingredients.id')),
        Column('amount', Float)
    )
    
    op.create_table(
        'unit',
        Column('id', Integer, primary_key=True),
        Column('name', String),
    )
    
    op.create_table(
        'ingredient',
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('unit_id', Integer, ForeignKey('units.id')),
    )
    
    op.create_table(
        'dish',
        Column('id', Integer, primary_key=True),
        Column('name', String),
    )


def downgrade() -> None:
    op.drop_table('dish_ingredient')
    op.drop_table('unit')
    op.drop_table('ingredient')
    op.drop_table('dish')
