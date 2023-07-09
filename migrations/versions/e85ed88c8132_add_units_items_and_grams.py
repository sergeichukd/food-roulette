"""add units items and grams

Revision ID: e85ed88c8132
Revises: fbf7995ae830
Create Date: 2023-07-09 20:38:32.873248

"""
import sqlalchemy as sa
from alembic import op

from app.models import Unit

# revision identifiers, used by Alembic.
revision = 'e85ed88c8132'
down_revision = 'fbf7995ae830'
branch_labels = None
depends_on = None


new_unit_names = ['items', 'gramms']

def upgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind)
    
    new_units = [Unit(name=n) for n in new_unit_names]
    
    session.add_all(new_units)    
    session.commit()

def downgrade() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind)
    session.query(Unit).filter(Unit.name.in_(new_unit_names)).delete()
    
    session.commit()
