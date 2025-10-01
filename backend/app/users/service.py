from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import User

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(db: AsyncSession, name: str):
    user = User(name=name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
