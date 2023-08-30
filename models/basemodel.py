
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class OrgBase(SQLModel):
    orgid: int
    name: str
    create_time: datetime = Field(default=datetime.now())


class PeopelBase(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str]
    create_time: datetime = Field(default=datetime.now())


class SiteBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = "微信公众号"
    create_time: datetime = Field(default=datetime.now())
