
from datetime import datetime
from enum import Enum
from type import Optional
from sqlmodel import SQLModel, Field


class frequency_type(str, Enum):
    day = 'd'
    week = 'w'
    q = 'q'
    half_year = '2q'
    year = 'y'
    unknown = 'none'


class edb_info(SQLModel):
    id: Optional[str] = Field(defalte=None, primary_key=True)
    create_time: datetime = Field(default=datetime.datetime.now())
    name: str
    start_time: datetime
    end_time: datetime
    source: str
    frequence: frequency_type.Enum
    isvalid: bool = Field(default=1)


class edb_data(SQLModel):
    id: Optional[str] = Field(defalte=None, primary_key=True)
    index: edb_info.id
    declaredate: datetime
    date: datetime
    value: str
    isvalid: bool = Field(default=1)
