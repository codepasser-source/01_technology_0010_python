#!/usr/bin/python3
# file name: sample_vo.py
# author: codepasser
# date: 2022/9/16
from pydantic import BaseModel


class SampleVo(BaseModel):
    """
    内置方法, DICT 转 OBJ
    """

    id: int = None
    name: str = None
    age: int = None
    create_time: str = None
    update_time: str = None
