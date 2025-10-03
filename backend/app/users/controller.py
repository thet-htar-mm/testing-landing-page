from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from . import service
from .schemas import UserOut
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=List[UserOut])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await service.get_users(db)

@router.post("/", response_model=UserOut)
async def add_user(name: str, db: AsyncSession = Depends(get_db)):
    return await service.create_user(db, name)
