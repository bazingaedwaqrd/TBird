# -*- coding: utf-8 -*-
"""
Created on 2016.9.11
@author: qkx
@description: Thunder Database with SQL Server
"""
import pyodbc

class TDB():
    """ TDB：读取SQL Server的数据类（只有读取功能） """
    def __init__(self,db_config):
        config = r'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' \
                 %(db_config['SERVER'],db_config['DATABASE'],db_config['UID'],db_config['PWD'])
        self._conn = pyodbc.connect(config)
        self._cursor = self._conn.cursor()
        
    def __del__(self):
        self._conn.close()

    def query(self,sql):
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        return result
