# coding=utf-8
from sqlalchemy import create_engine
import pandas as pd
# import pymssql
# DB = pymssql.connect(server='127.0.0.1',user='sa',password='Chinkun65613303',database='tsqx')
a = {'1':232}
for item,val in a.iteritems():
    print item,val
# sqldb = 'mssql+pymssql://sa:Chinkun65613303@localhost/test'
# engine = create_engine(sqldb)
# print pd.read_sql_query('select * from test.dbo.THUNDER',engine)

# class Thunder(db.Model):
#     time = db.Column(db.DATETIME,primary_key=True)
#     lon = db.Column(db.REAL)
#     lat =  db.Column(db.REAL)
#
#     def __init__(self,time,lat,lon):
#         self.time = time
#         self.lat = lat
#         self.lon = lon
# td1 = Thunder('20150612',120,20)
# td2 = Thunder('20150612',120,20)
# db.session.add(td1)
# print Thunder.query.all()
# print Thunder.query.all()