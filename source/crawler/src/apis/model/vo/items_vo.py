#!/usr/bin/python3
# file name: sample_vo.py
# author: codepasser
# date: 2022/9/16
from typing import List
from pydantic import BaseModel

from src.apis.model.vo.item_vo import ItemVo


class ItemsVo(BaseModel):
    data: List[ItemVo] = []

    def __init__(self, data: List[ItemVo]):
        super().__init__()
        self.data = data
