#!/usr/bin/python3
# file name: funs.py
# author: codepasser
# date: 2022/9/21
import time

from src.configuration.datasource.mybatis.sql_util import *


def like(value):
    return sql_string_format('%{}%'.format(value))


def time_format(date_value, format: str = '%Y-%m-%d %H:%M:%S'):
    return sql_string_format(time.strftime(format, date_value))


default_fun_dict = {'like': like, 'time_format': time_format}
