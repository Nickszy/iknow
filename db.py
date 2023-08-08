
from typing import List
import pandas as pd
from sqlmodel import create_engine, SQLModel

url = "postgresql://fin:ceshi001@localhost:5432/finplan_test"

engine = create_engine(url)


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
