#!/usr/bin/python3
# file name: sample_bo.py
# author: codepasser
# date: 2022/9/16
from pydantic import BaseModel


class SampleBo(BaseModel):
    id: int = None
    name: str = None
    age: int = None

    def __init__(self, name, age, id: int = None) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.age = age

    """
    当对实例化对象使用dict(obj)的时候, 会调用这个方法,
    这里定义了字典的键, 其对应的值将以obj['name']的形式取,
    但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法
    """

    @staticmethod
    def keys():
        return 'id', 'name', 'age'

    """
    内置方法, OBJ 转 DICT
    """

    def __getitem__(self, item):
        return getattr(self, item)
