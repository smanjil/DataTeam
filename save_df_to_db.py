
import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:12345@localhost/datateamdb')

df = pd.read_csv('input/finalapi.csv')

# detailed information storage
df.to_sql('detailed_table', engine, if_exists = 'append', index = False)