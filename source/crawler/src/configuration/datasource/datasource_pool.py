#!/usr/bin/python3
# file name: db_pool.py
# author: codepasser
# date: 2022/9/21
from dbutils.pooled_db import PooledDB
import pymysql
from src.configuration import ConfigAppIni, Singleton


@Singleton
class DataSourcePool(object):
    datasource: PooledDB

    def __init__(self):
        config_app_ini = ConfigAppIni()
        self.datasource = PooledDB(
            creator=pymysql,
            cursorclass=pymysql.cursors.DictCursor,
            host=config_app_ini.get('datasource', 'host'),
            port=int(config_app_ini.get('datasource', 'port')),
            user=config_app_ini.get('datasource', 'user'),
            password=config_app_ini.get('datasource', 'password'),
            database=config_app_ini.get('datasource', 'database'),
            charset=config_app_ini.get('datasource', 'charset'),
            ping=int(config_app_ini.get('datasource', 'ping')),
            maxconnections=int(config_app_ini.get('datasource', 'max_connections')),
            mincached=int(config_app_ini.get('datasource', 'min_cached')),
            maxcached=int(config_app_ini.get('datasource', 'max_cached')),
            blocking=True,
            maxusage=None,
            setsession=[]
        )

    def get_datasource(self):
        return self.datasource
