
from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class frequency_type(str, Enum):
    day = 'd'
    week = 'w'
    q = 'q'
    half_year = '2q'
    year = 'y'
    unknown = 'none'


class edb_info(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    create_time: datetime = Field(default=datetime.now())
    name: str
    start_time: datetime
    end_time: datetime
    source: str
    frequence: frequency_type
    isvalid: bool = Field(default=1)


class edb_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    index: int = Field(foreign_key="edb_info.id")
    declaredate: datetime
    date: datetime
    value: str
    isvalid: bool = Field(default=1)
