from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from . import service

router = APIRouter(prefix="/users", tags=["users"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/")
async def list_users(db: AsyncSession = Depends(get_db)):
    return await service.get_users(db)

@router.post("/")
async def add_user(name: str, db: AsyncSession = Depends(get_db)):
    return await service.create_user(db, name)
