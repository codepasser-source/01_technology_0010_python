#!/usr/bin/python3
# file name: math.py
# author: codepasser
# date: 2022/9/6
from decimal import Decimal
from typing import List


class Math:
    __scale: str = None

    def __init__(self, scale: str = '0.0000'):
        self.__scale = scale

    def fixed(self, _item: float) -> float:
        """
        保留有效数字
        :param _item: 值
        :return: 结果
        """
        return float(Decimal('%16f' % _item).quantize(Decimal(self.__scale)))

    def fixed_multi(self, _items: List[float]) -> List[float]:
        """
        保留有效数字（数组全部元素）
        :param _items: 值-数组
        :return: 结果-数组
        """
        _result: List[float] = []
        for i in range(len(_items)):
            _fixed = self.fixed(_items[i])
            _result.append(_fixed)
        return _result

    def is_integer(self, _val) -> bool:
        """
        是否为整数值
        :param _val: 值
        :return: 结果
        """
        _val = Decimal('%16f' % _val).quantize(Decimal(self.__scale))
        _count_dot = str(_val).count('.')
        if _count_dot == 0:
            return True
        _s_val = str(_val).split('.')
        if len(_s_val) == 1:
            return True
        if len(_s_val) == 2 and _s_val[1] == '0000':
            return True
        else:
            return False
