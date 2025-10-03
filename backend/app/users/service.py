from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def get_users(db: AsyncSession):
    query = text("SELECT * FROM users")
    result = await db.execute(query)
    return result.fetchall()


async def create_user(db: AsyncSession, name: str):
    insert_query = text("""
        INSERT INTO users (name)
        VALUES (:name)
        RETURNING *
    """)
    result = await db.execute(insert_query, {"name": name})
    await db.commit()
    return result.fetchone()
