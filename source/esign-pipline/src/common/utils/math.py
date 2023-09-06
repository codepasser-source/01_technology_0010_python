#!/usr/bin/python3
# file name: math.py
# author: codepasser
# date: 2022/9/6
from decimal import Decimal
from typing import List

import numpy as np


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

    @staticmethod
    def computed_ln(_items: List[float]) -> List[float]:
        """
        注意点：若样本中含有0或负数无需取ln值
        保留有效数字（数组全部元素）并计算数组数据的ln值
        :param _items: 值-数组
        :return: 结果-数组
        """
        _result: List[float] = []
        for i in range(len(_items)):
            _ln_result = np.log(_items[i])
            _result.append(_ln_result)
        return _result

    @staticmethod
    def computed_ln_current(_item: float) -> float:
        """
        注意点：若样本中含有0或负数无需取ln值
        计算当前数据的ln值
        :param _item: 值-当前值
        :return: 结果-当前值取对数
        """
        return np.log(_item)

    @staticmethod
    def is_computed_ln(_items: List[float]) -> bool:
        """
        直接获取列表最小数值 判断其是否 > 0
        :param _items: 值-数组
        :return: 结果-最小值是否是正数
        """
        return min(_items) > 0 if _items else False

    @staticmethod
    def sub_abs(_items: List[float], _field_avg: float) -> List[float]:
        """
        综合指标：
            i.以50%为界限，所有数据减去50%，再取绝对值，做标准正态，越小越好；
            ii.以行业平均为界限，分行业取平均值，所有数据减去所在行业的平均值，再取绝对值，做标准正态，越小越好；
        :param _items: 值-数组
        :param _field_avg: 值-所在行业平均值
        :return: 结果-数组
        """
        _result: List[float] = []
        for i in range(len(_items)):
            _sub_result = abs(_items[i] - _field_avg)
            _result.append(_sub_result)
        return _result

    @staticmethod
    def sub_abs_current(_item: float, _field_avg: float) -> float:
        """
        综合指标：
            i.以50%为界限，所有数据减去50%，再取绝对值，做标准正态，越小越好；
            ii.以行业平均为界限，分行业取平均值，所有数据减去所在行业的平均值，再取绝对值，做标准正态，越小越好；
        :param _item: 值-当前值
        :param _field_avg: 值-所在行业平均值
        :return: 结果-当前值取减平均值 取对数
        """
        return abs(_item - _field_avg)
