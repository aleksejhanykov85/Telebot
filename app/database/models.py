from sqlalchemy import BigInteger, String, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    diseases: Mapped[str] = mapped_column(String(120))
    preferences: Mapped[str] = mapped_column(String(120))
    current_weight: Mapped[int] = mapped_column()
    desired_weight: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
    num_of_days: Mapped[int] = mapped_column()
    time: Mapped[Time] = mapped_column(Time)
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)