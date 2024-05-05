from datetime import datetime

from pydantic import BaseModel


class IndicatorDTO(BaseModel):
    date: datetime
    value: int

    # id = Column(Integer, primary_key=True, index=True)
    # date = Column(DateTime, unique=True, index=True)
    # value = Column(Integer)
    # published = Column(Boolean, default=False),
    # created_on = Column(DateTime, default=datetime.now),
    # updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
