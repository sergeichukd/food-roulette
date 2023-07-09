from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

dish_ingredient = Table(
    'dish_ingredient',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dish.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('amount', Float)
    )

class Unit(Base):
    __tablename__ = 'unit'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return str(vars(self))

class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    dishes = relationship('Dish', secondary=dish_ingredient, back_populates='ingredients')
    
    def __repr__(self):
        return str(vars(self))
    
class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = relationship('Ingredient', secondary=dish_ingredient, back_populates='dishes')
    
    def __repr__(self):
        return str(vars(self))
