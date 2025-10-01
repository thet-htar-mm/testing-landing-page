from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Post

async def get_posts(db: AsyncSession):
    result = await db.execute(select(Post))
    return result.scalars().all()

async def create_post(db: AsyncSession, title: str, content: str, user_id: int):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post
