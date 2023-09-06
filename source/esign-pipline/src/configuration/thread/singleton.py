#!/usr/bin/python3
# file name: singleton.py
# author: codepasser
# date: 2022/11/19
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
