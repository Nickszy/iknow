
from typing import List
import pandas as pd
from sqlmodel import SQLModel, create_engine, Session, select

# mysql_url = "mysql+pymysql://iknow:iknow@localhost:3306/iknow"
sqlite_url = "sqlite:///datebase.db"
engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def sqlmodel_to_df(objects: List[SQLModel]) -> pd.DataFrame:
    """Converts SQLModel objects into a Pandas DataFrame.
    Usage
    ----------
    df = sqlmodel_to_df(list_of_sqlmodels)
    Parameters
    ----------
    :param objects: List[SQLModel]: List of SQLModel objects to be converted.
    """

    return pd.DataFrame.from_records(map(dict, objects)).iloc[:, 1:]


# if __name__ == "__main__":
#     from models import *
#     # create_db_and_tables()
