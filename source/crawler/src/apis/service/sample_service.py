#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/9/21
from typing import Optional

from fastapi import Response, status

from src.configuration import Page
from src.apis.model import AssertResponse, SampleBo, SampleVo
from src.apis.repository.mapper.sample_mapper import SampleMapper


class SampleService(object):
    __sample_mapper: SampleMapper

    def __init__(self):
        self.__sample_mapper = SampleMapper()

    def creation(self, _item: SampleBo, response: Response) -> AssertResponse:
        _result: int = self.__sample_mapper.creation(_item)
        return AssertResponse(_result > 0)

    def deletion(self, _id: int, response: Response) -> AssertResponse:
        _result: int = self.__sample_mapper.deletion(_id)
        return AssertResponse(_result > 0)

    def modify(self, _item: SampleBo, response: Response) -> AssertResponse:
        _result: int = self.__sample_mapper.modify(_item)
        return AssertResponse(_result > 0)

    def detail(self, _id: int, response: Response) -> Optional[SampleVo]:
        data: SampleVo = self.__sample_mapper.detail(_id)
        if data is not None:
            return data
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return None

    def page(self, keyword: str, page_num: int, page_size: int, response: Response) -> Page:
        return self.__sample_mapper.page(keyword, page_num, page_size)
