from app.database.models import async_session
from app.database.models import User, Info_User
from sqlalchemy import select, update


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def add_info_user(data,tg_id):
    async with async_session() as session:
        info = await session.scalar(select(Info_User).where(Info_User.user == tg_id))

        if not info:
            info_user = Info_User(
                age=data["age"],
                sex=data["sex"],
                physical_activity=data["physical_activity"],
                diseases=data["diseases"],
                preferences=data["preferences"],
                current_weight=data["current_weight"],
                desired_weight=data["desired_weight"],
                height=data["height"],
                number_of_meals = data["number_of_meals"],
                cost = data["cost"],
                user=tg_id
            )
            session.add(info_user)
        
        else:
        
            await session.execute(update(Info_User).where(Info_User.user == tg_id).values(
                age=data["age"],
                sex=data["sex"],
                physical_activity=data["physical_activity"],
                diseases=data["diseases"],
                preferences=data["preferences"],
                current_weight=data["current_weight"],
                desired_weight=data["desired_weight"],
                height=data["height"],
                number_of_meals = data["number_of_meals"],
                cost = data["cost"]
            ))

        await session.commit()
        

async def add_new_pref(new,tg_id):
    async with async_session() as session:
        stmt = select(Info_User.preferences).where(Info_User.user == tg_id)
        check = str(*await get_pref(tg_id)) 
        if check == "-":
            update_stmt = (
            update(Info_User)
            .where(Info_User.user == tg_id)
            .values(preferences="")
        )
            await session.execute(update_stmt)
            await session.commit()

        result = await session.execute(stmt)
        current_prefs = str(*result.scalars().all())
        if current_prefs == "":
            updated_prefs = new 
        else:
            updated_prefs = current_prefs + ',' + new 
        update_stmt = (
            update(Info_User)
            .where(Info_User.user == tg_id)
            .values(preferences=updated_prefs)
        )
        await session.execute(update_stmt)
        await session.commit()
        return str(*await get_pref(tg_id))
    

async def add_new_dis(new,tg_id):
    async with async_session() as session:
        stmt = select(Info_User.diseases).where(Info_User.user == tg_id)
        check = str(*await get_dis(tg_id)) 
        if check == "-":
            update_stmt = (
            update(Info_User)
            .where(Info_User.user == tg_id)
            .values(diseases="")
        )
            await session.execute(update_stmt)
            await session.commit()

        result = await session.execute(stmt)
        current_dis = str(*result.scalars().all())
        if current_dis == "":
            updated_dis = new 
        else:
            updated_dis = current_dis + ',' + new 
        update_stmt = (
            update(Info_User)
            .where(Info_User.user == tg_id)
            .values(diseases=updated_dis)
        )
        await session.execute(update_stmt)
        await session.commit()
        return str(*await get_dis(tg_id))


async def get_info_user(tg_id):
    async with async_session() as session:
        stmt = select(Info_User).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().all()
        return user_info
    

async def get_current_weight(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.current_weight).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info
    

async def get_desired_weight(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.desired_weight).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info


async def get_sex(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.sex).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info
    

async def get_age(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.age).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info
    

async def get_height(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.height).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info
    

async def get_phys_act(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.physical_activity).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().first()
        return user_info
    

async def get_pref(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.preferences).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().all()
        return user_info
    

async def get_dis(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.diseases).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().all()
        return user_info
    

async def get_num_of_meals(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.number_of_meals).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().all()
        return user_info
    

async def get_cost(tg_id):
    async with async_session() as session:
        stmt = select(Info_User.cost).where(Info_User.user == tg_id)
        result = await session.execute(stmt)
        user_info = result.scalars().all()
        return user_info