
from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class node(SQLModel):
    '''
    id = 1 为根节点
    '''
    id: Optional[str] = Field(default=None, primary_key=True)
    name: str


class node_relation(SQLModel):
    id: Optional[str] = Field(default=None, primary_key=True)
    strat_nodeid: int = Field(default=None, foreign_key="node.id")
    end_nodeid: int = Field(default=None, foreign_key="node.id")


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
    des: str
    start_time: datetime
    end_time: datetime
    source: str
    frequence: frequency_type
    isvalid: bool = Field(default=1)


class edb_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    index: int = Field(foreign_key="edb_info.id")
    edb_id: int = Field(default=None, foreign_key="edb_info.id", index=True)
    declaredate: datetime
    date: datetime
    value: str
    isvalid: bool = Field(default=1)
