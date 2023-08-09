# How to make relationships: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html

from typing import List

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class Base(DeclarativeBase):
    pass


class DishIngredient(Base):
    __tablename__ = 'dish_ingredient'

    dish_id: Mapped[int] = mapped_column(ForeignKey('dish.id'), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey('ingredient.id'), primary_key=True)

    amount: Mapped[float]

    dish: Mapped['Dish'] = relationship(back_populates='ingredients')
    ingredient: Mapped['Ingredient'] = relationship(back_populates='dishes')

    def __repr__(self) -> str:
        return str(vars(self))


class Unit(Base):
    __tablename__ = 'unit'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def __repr__(self) -> str:
        return str(vars(self))


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    unit_id: Mapped[int] = mapped_column(ForeignKey('unit.id'))
    name: Mapped[str] = mapped_column()
    unit: Mapped[Unit] = relationship()
    dishes: Mapped[List[DishIngredient]] = relationship(back_populates='ingredient')

    def __repr__(self) -> str:
        return str(vars(self))


class Dish(Base):
    __tablename__ = 'dish'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    ingredients: Mapped[List[DishIngredient]] = relationship(back_populates='dish')

    def __repr__(self) -> str:
        return str(vars(self))


if __name__ == '__main__':
    engine = create_engine("sqlite:///tmp.db")
    Base.metadata.create_all(engine)

    session = Session(engine)

    # create unit
    gramm = Unit(name='gramm')
    item = Unit(name='item')

    session.add_all([gramm, item])
    session.commit()

    # create dish
    potato = Ingredient(name='potato', unit=item)
    salt = Ingredient(name='salt', unit=gramm)

    ponfrit = Dish(name='ponfrit')
    ponfrit.ingredients.append(DishIngredient(amount=12.43, ingredient=potato))
    ponfrit.ingredients.append(DishIngredient(amount=1.2, ingredient=salt))

    session.add(ponfrit)
    session.commit()

    print()
