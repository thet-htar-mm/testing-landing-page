from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def get_posts(db: AsyncSession):
    query = text("""
        SELECT 
            posts.id AS post_id,
            posts.title AS post_title,
            posts.content AS post_content,
            users.id AS user_id,
            users.name AS user_name
        FROM posts
        JOIN users ON posts.user_id = users.id
    """)
    result = await db.execute(query)
    rows = result.fetchall()

    posts = []
    for row in rows:
        post_dict = {
            "id": row.post_id,
            "title": row.post_title,
            "content": row.post_content,
            "user": {
                "id": row.user_id,
                "name": row.user_name
            }
        }
        posts.append(post_dict)
    return posts

async def create_post(db: AsyncSession, title: str, content: str, user_id: int):
    insert_query = text("""
        INSERT INTO posts (title, content, user_id)
        VALUES (:title, :content, :user_id)
        RETURNING *
    """)
    
    result = await db.execute(insert_query, {
        "title": title,
        "content": content,
        "user_id": user_id
    })

    await db.commit()

    new_post = result.fetchone()
    return new_post
