from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from . import service
from typing import List
from .models import PostOut

router = APIRouter(prefix="/posts", tags=["posts"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=List[PostOut])
async def list_posts(db: AsyncSession = Depends(get_db)):
    return await service.get_posts(db)

@router.post("/", response_model=PostOut)
async def add_post(title: str, content: str, user_id: int, db: AsyncSession = Depends(get_db)):
    return await service.create_post(db, title, content, user_id)
