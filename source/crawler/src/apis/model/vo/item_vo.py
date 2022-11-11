#!/usr/bin/python3
# file name: snd_item_vo.py
# author: codepasser
# date: 2022/9/16
from pydantic import BaseModel


class ItemVo(BaseModel):
    key: str = None
    val: float = None

    def __init__(self, key: str, val: float):
        super().__init__()
        self.key = key
        self.val = val
