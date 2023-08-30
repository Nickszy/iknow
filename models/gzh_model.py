
from datetime import datetime
from typing import Optional

from pydantic import AnyHttpUrl
from sqlmodel import Field, SQLModel

from models.basemodel import SiteBase


class gzh_info(SiteBase, table=True):
    bookId: str
    title: str
    description: str
    author: str
    cover: Optional[AnyHttpUrl]
    bookStatus: bool = 1
    finished: bool = 1
    language: str = 'zh'
    rate: int = 0


class mp_info(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    originalId: int = Field(foreign_key='gzh_info.id')
    doc_url: AnyHttpUrl
    pic_url: AnyHttpUrl
    title: str
    avatar: AnyHttpUrl
    content: str
    time: datetime
