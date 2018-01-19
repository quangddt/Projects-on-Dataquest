# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import psycopg2 as ps2
import pandas as pd

conn = ps2.connect(database='quang', user='quang', password='524784kinG!', host='127.0.0.1')
query = "SELECT * FROM notes";
data = pd.read_sql_query(query, conn)
print(data)
conn.close()