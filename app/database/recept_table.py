from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///recept_and_ingredients.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Recept(Base):
    __tablename__ = 'Recepts'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    portions: Mapped[int] = mapped_column(Integer)
    calories: Mapped[int] = mapped_column(Integer)
    proteins: Mapped[int] = mapped_column(Integer)
    fats: Mapped[int] = mapped_column(Integer)
    carbohydrates: Mapped[int] = mapped_column(Integer)
    cat_id: Mapped[int] = mapped_column(ForeignKey('Categories.id'), primary_key=True)


class Ingredient(Base):
    __tablename__ = 'Ingredients'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)
    quantity_per_package: Mapped[int] = mapped_column(Integer)


class Rec_and_Ing(Base):
    __tablename__ = 'Recs&Ings'
    
    recipe_id: Mapped[int] = mapped_column(ForeignKey('Recepts.id'), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey('Ingredients.id'), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    
    
class Category(Base):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    
    
async def async_rec_and_ings():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    