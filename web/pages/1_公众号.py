from db import *
from models import gzh_info
import streamlit as st
st.set_page_config(layout="wide")

with Session(engine) as session:
    sql = select(gzh_info)
    results = session.exec(sql).all()
    sqlmodel_to_df(results)
st.dataframe(sqlmodel_to_df(results))
