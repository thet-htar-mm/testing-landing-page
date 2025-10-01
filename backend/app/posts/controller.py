from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from . import service

router = APIRouter(prefix="/posts", tags=["posts"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/")
async def list_posts(db: AsyncSession = Depends(get_db)):
    return await service.get_posts(db)

@router.post("/")
async def add_post(title: str, content: str, user_id: int, db: AsyncSession = Depends(get_db)):
    return await service.create_post(db, title, content, user_id)
