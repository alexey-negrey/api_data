from datetime import datetime

from sqlalchemy.orm import Session

from dto import IndicatorDTO
from models import Indicator, Mode
from setting import ST_PASSWORD


def create_value(db: Session, data: IndicatorDTO):
    if not check_mode(db):
        return '{"mode": 0}'
    value = Indicator(date=data.date, value=data.value, published=True)
    try:
        db.add(value)
        db.commit()
        db.refresh(value)
    except Exception as e:
        print(e)

    return value


def get_value(db: Session, value_id: int):
    if not check_mode(db):
        return '{"mode": 0}'
    return db.query(Indicator).filter(Indicator.id == value_id).first()


# def get_values(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Indicator).offset(skip).limit(limit).all()

def get_values(db: Session):
    if not check_mode(db):
        return '{"mode": 0}'
    return db.query(Indicator).order_by(Indicator.date.desc()).all()


def remove_value(db: Session, value_id: int):
    if not check_mode(db):
        return '{"mode": 0}'
    value = db.query(Indicator).filter(Indicator.id == value_id).delete()
    db.commit()
    return value


def update_value(db: Session, value_id: int, data: IndicatorDTO):
    if not check_mode(db):
        return '{"mode": 0}'
    value = db.query(Indicator).filter(Indicator.id == value_id).first()
    value.value = data.value
    value.date = data.date
    try:
        db.add(value)
        db.commit()
        db.refresh(value)
    except Exception as e:
        print(e)

    return value


def get(db: Session, date: datetime):
    """ Получение показателя на дату """
    value = db.query(Indicator).filter(Indicator.date <= date).order_by(Indicator.date.desc()).first()
    if value:
        result = [{'date': value.date, 'value': value.value}]
    else:
        result = [{'date': date, 'value': None}]
        value = db.query(Indicator).filter(Indicator.date > date).order_by(Indicator.date).first()
        if value:
            result.append({'date': value.date, 'value': value.value})
    return result


def change_mode(db: Session, pmode: int, pw: str):
    if pw == ST_PASSWORD:
        value = Mode(value=True if pmode == 1 else False)
        try:
            db.add(value)
            db.commit()
            db.refresh(value)
        except Exception as e:
            print(e)

        return value
    else:
        return '{}'

def check_mode(db: Session) -> bool:
    value = db.query(Mode).order_by(Mode.date.desc()).first()
    if value:
        return value.value
    else:
        return True
