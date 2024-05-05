from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import services as IService
from database import get_db
from dto import IndicatorDTO

router = APIRouter()

@router.get('/set', tags=['mode'])
async def set_mode(mode: int = None, pw: str = None, db: Session = Depends(get_db)):
    return IService.change_mode(db, mode, pw)


@router.post('/add', tags=['indicator'])
async def add_value(data: IndicatorDTO, db: Session = Depends(get_db)):
    return IService.create_value(db, data)


@router.get('/value', tags=['indicator'])
async def get_value(date: datetime, db: Session = Depends(get_db)):
    return IService.get(db, date)


@router.get('/all_value', tags=['indicator'])
async def get_all_value(db: Session = Depends(get_db)):
    return IService.get_values(db)


@router.get('/{id}', tags=['indicator'])
async def get_by_id(id: int = None, db: Session = Depends(get_db)):
    return IService.get_value(db, id)


@router.delete('/{id}', tags=['indicator'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return IService.remove_value(db, id)


@router.put('/{id}', tags=['indicator'])
async def update(id: int = None, data: IndicatorDTO = None, db: Session = Depends(get_db)):
    return IService.update_value(db, id, data)


