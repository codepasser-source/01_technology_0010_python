#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/11
from typing import Optional

from src.configuration import Page
from src.apis.model import SampleBo, SampleVo
from src.apis.repository.mapper.sample_mapper import SampleMapper


class SampleCell(object):
    __sample_mapper: SampleMapper

    def __init__(self):
        self.__sample_mapper = SampleMapper()

    def creation(self, _item: SampleBo) -> bool:
        _result: int = self.__sample_mapper.creation(_item)
        return _result > 0

    def deletion(self, _id: int) -> bool:
        _result: int = self.__sample_mapper.deletion(_id)
        return _result > 0

    def modify(self, _item: SampleBo) -> bool:
        _result: int = self.__sample_mapper.modify(_item)
        return _result > 0

    def detail(self, _id: int) -> Optional[SampleVo]:
        data: SampleVo = self.__sample_mapper.detail(_id)
        if data is not None:
            return data
        else:
            return None

    def page(self, keyword: str, page_num: int, page_size: int) -> Page:
        return self.__sample_mapper.page(keyword, page_num, page_size)
