#!/usr/bin/python3
# file name: sample_vo.py
# author: codepasser
# date: 2022/9/16

class SampleVo(dict):
    """
    内置方法, DICT 转 OBJ
    """

    def __getattr__(self, key):
        if key not in self:
            return None
        else:
            value = self[key]
            if isinstance(value, dict):
                value = SampleVo(value)
                return value
