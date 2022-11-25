#!/usr/bin/python3
# author: codepasser
# date: 2022/02/15

import datetime

import time


def get_time(ms=False):
    return datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M:%S{r".%f" if ms else ""}')


def get_timestamp(_ms=False):
    _now_timestamp = time.time()
    return _now_timestamp if _ms else int(_now_timestamp)


def convert_time(_timestamp, _ms=False):
    _time_tuple = datetime.datetime.utcfromtimestamp(_timestamp)
    return _time_tuple.strftime(f'%Y-%m-%d %H:%M:%S{r".%f" if _ms else ""}')


def convert_timestamp(_time_str):
    if '.' not in _time_str:
        _ms = False
    else:
        _ms = True
    _time_tuple = datetime.datetime.strptime(_time_str, f'%Y-%m-%d %H:%M:%S{r".%f" if _ms else ""}')
    _timestamp = float(f'{str(int(time.mktime(_time_tuple.timetuple())))}' + (f'.{_time_tuple.microsecond}' if _ms else ''))
    return _timestamp if _ms else int(_timestamp)
