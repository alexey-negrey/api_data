from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean

from database import Base


class Indicator(Base):
    __tablename__ = 'indicator'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, unique=True, index=True)
    value = Column(Integer)
    published = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Mode(Base):
    __tablename__ = 'mode'
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Boolean)
    date = Column(DateTime, default=datetime.now)