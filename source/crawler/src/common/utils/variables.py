#!/usr/bin/python3
# file name: variables.py
# author: codepasser
# date: 2022/11/16
from typing import Optional


class Variables:

    @staticmethod
    def replace(_expression: str, _var: dict) -> str:
        """
        表达式替换
        :param _expression: 表达式
        :param _var: 值
        :return: 结果
        """
        return _expression % _var

    @staticmethod
    def dict_replace(_data: dict, _var: dict) -> Optional[dict]:
        """
        表达式替换
        :param _data: 字典
        :param _var: 值
        :return: 结果
        """
        if _data is None:
            return None

        _clone: dict = {}
        for _key in _data.keys():
            _value = Variables.replace(_data.get(_key), _var)
            _clone[_key] = _value
        return _clone
