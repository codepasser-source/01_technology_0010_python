#!/usr/bin/python3
# file name: dicts.py
# author: codepasser
# date: 2022/11/16
from typing import List


class Dicts:

    @staticmethod
    def dict_mapper(_data: dict, _mapper: str):
        _mappers: List[str] = _mapper.split('.')

        _data_val = _data
        for _index in range(len(_mappers)):
            _mapping: str = _mappers[_index]
            _data_val = Dicts.dict_value(_data_val, _mapping)
        # outside for
        return _data_val

    @staticmethod
    def dict_value(_value: dict, _mapping: str):
        if _value is not None:
            if type(_value) is dict:
                return _value[_mapping]
            if type(_value) is list:
                return _value[int(_mapping)]
        else:
            return None
