from pprint import pprint
import sys
from models import gzh_info

from db import *
import base64
import streamlit as st
import numpy as np
from web.utils import add_logo
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
add_logo("web\img\my_logo.jpg")
st.markdown("# Home")
# create_db_and_tables()

# st.dataframe(db.sqlmodel_to_df(results))

with Session(engine) as session:
    sql = select(gzh_info)
    results = session.exec(sql).all()
    sqlmodel_to_df(results)
st.dataframe(sqlmodel_to_df(results))
