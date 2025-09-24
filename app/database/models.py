from sqlalchemy import BigInteger, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import datetime

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tg_id = mapped_column(BigInteger)
    active = mapped_column(Boolean, default=True)


class Info_User(Base):
    __tablename__ = 'Info_User'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    age: Mapped[int] = mapped_column()
    sex: Mapped[str] = mapped_column()
    physical_activity: Mapped[int] = mapped_column()
    diseases: Mapped[str] = mapped_column(String(120))
    preferences: Mapped[str] = mapped_column(String(120))
    current_weight: Mapped[str] = mapped_column(String(7))
    desired_weight: Mapped[str] = mapped_column(String(7))
    height: Mapped[str] = mapped_column(String(7))
    number_of_meals: Mapped[int] = mapped_column()
    cost: Mapped[int] = mapped_column()
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))


class Broadcast(Base):
    __tablename__ = 'broadcast'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    message = mapped_column(String, nullable=False)
    sent_at = mapped_column(DateTime, default=datetime.datetime.now)
    
async def async_user():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)