"""initialize

Revision ID: fbf7995ae830
Revises: 
Create Date: 2023-07-09 16:14:09.131918

"""
import sqlalchemy as sa
from alembic import op
from app.models import Dish, Unit, Ingredient, dish_ingredient


# revision identifiers, used by Alembic.
revision = 'fbf7995ae830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session()
    
    # Create tables
    Unit.__table__.create(bind)
    Dish.__table__.create(bind)
    Ingredient.__table__.create(bind)
    dish_ingredient.create(bind)
    session.commit()


def downgrade() -> None:
    op.drop_table('dish_ingredient')
    op.drop_table('unit')
    op.drop_table('ingredient')
    op.drop_table('dish')
