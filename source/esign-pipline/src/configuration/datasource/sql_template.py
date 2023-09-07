#!/usr/bin/python3
# file name: mybatis_sql_template.py
# author: codepasser
# date: 2022/9/20

import contextlib
from pydantic import BaseModel
from dbutils.pooled_db import PooledDB

from src.configuration import ConfigLogger, DataSourcePool

CONSOLE_LOGGER = ConfigLogger.console_log()


class Page(BaseModel):
    size: int = None
    page: int = None
    total: int = None
    data: list = []

    def __init__(self, size: int = None, page: int = None, total: int = None, data: list = None):
        super().__init__()
        self.size = size
        self.page = page
        self.total = total
        self.data = data


class RowBound(object):
    def __init__(self, page: int, size: int):
        self.page = page
        self.size = size


"""
基本操作:增删改查,分页
"""


class SqlTemplate(object):
    datasource: PooledDB

    def __init__(self):
        self.datasource = DataSourcePool().get_datasource()

    """

    when con is not None 
    must be commit manually by the calling function

    """

    def select_one(self, sql: str, con=None, args=None):
        with self.get_connection(con) as connection:
            cursor = connection.cursor()
            CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            # print('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            cursor.execute(sql, args)
            data = cursor.fetchone()
            cursor.close()
            return data

    def select_list(self, sql: str, row_bound: RowBound = None, con=None, args=None):
        with self.get_connection(con) as connection:
            cursor = connection.cursor()
            if row_bound:
                sql = limit_query(sql, row_bound)
            CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            # print('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            cursor.execute(sql, args)
            data = cursor.fetchall()
            cursor.close()
            return data

    def select_page(self, sql: str, count_sql: str = None, row_bound: RowBound = None, con=None, args=None):
        with self.get_connection(con) as connection:
            cursor = connection.cursor()
            page_result = Page()
            page_result.page = row_bound.page
            page_result.size = row_bound.size
            if count_sql is None:
                count_sql = count_query(sql)
                CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(count_sql, args))
                # print('[SQL:({})] - [ARGS:({})]'.format(count_sql, args))
                cursor.execute(count_sql, args)
                page_result.total = cursor.fetchone()['count(*)']
            else:
                cursor.execute(count_sql, args)
                CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(count_sql, args))
                # print('[SQL:({})] - [ARGS:({})]'.format(count_sql, args))
                page_result.total = get_one_value(cursor.fetchone())
            sql = limit_query(sql, row_bound)
            CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            # print('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            cursor.execute(sql, args)
            page_result.data = cursor.fetchall()
            cursor.close()
        return page_result

    def insert(self, sql: str, con=None, args=None):
        return self.update(sql, con, args)

    def insert_batch(self, sql: str, con=None, args=None):
        auto_commit = not con
        with self.get_connection(con) as connection:
            cursor = connection.cursor()
            CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            # print('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            data = cursor.executemany(sql, args)
            if auto_commit:
                connection.commit()
                cursor.close()
            return data

    def update(self, sql: str, con=None, args=None):
        auto_commit = not con
        with self.get_connection(con) as connection:
            cursor = connection.cursor()
            CONSOLE_LOGGER.debug('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            # print('[SQL:({})] - [ARGS:({})]'.format(sql, args))
            data = cursor.execute(sql, args)
            if auto_commit:
                connection.commit()
                cursor.close()
            return data

    def delete(self, sql, con=None, args=None):
        return self.update(sql, con, args)

    def execute_in_connection(self, fun):
        with self.get_connection() as con:
            return fun(con)

    @contextlib.contextmanager
    def get_connection(self, connection=None):
        auto_close = True
        if connection:
            auto_close = False
        else:
            connection = self.datasource.connection()
        try:
            yield connection
        except Exception:
            connection.rollback()
            raise
        finally:
            if auto_close:
                connection.close()


"""
分页查询
"""


def count_query(sql: str):
    return 'select count(*) from ( ' + sql + ' ) temp'


def limit_query(sql: str, row_bound: RowBound):
    start = (row_bound.page - 1) * row_bound.size
    return sql + ' limit {},{}'.format(start, row_bound.size)


def get_one_value(count_dict: dict):
    for count in count_dict.values():
        return count
