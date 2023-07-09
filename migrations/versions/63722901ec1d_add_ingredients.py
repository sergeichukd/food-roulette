"""add ingredients

Revision ID: 63722901ec1d
Revises: e85ed88c8132
Create Date: 2023-07-09 20:39:58.045993

"""
import sqlalchemy as sa
from alembic import op

from app.models import Ingredient, Unit

# revision identifiers, used by Alembic.
revision = '63722901ec1d'
down_revision = 'e85ed88c8132'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()    
    session = sa.orm.Session(bind)

    gramm_unit = session.query(Unit).filter_by(name='gramms').first()
    items_unit = session.query(Unit).filter_by(name='items').first()
    
    ingredients = [
        Ingredient(name='agg', unit_id=items_unit.id),
        Ingredient(name='salt', unit_id=gramm_unit.id),
    ]
    session.add_all(ingredients)
    session.commit()

def downgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind)
    num_objects = session.query(Ingredient).filter(Ingredient.name.in_(['agg', 'salt'])).delete()
    print(f'Remove {num_objects} objects')
    session.commit()
