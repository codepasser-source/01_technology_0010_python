#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/9/21
from typing import Optional

from fastapi import Response, status

from src.configuration import Page
from src.apis.model import AssertResponse, SampleBo, SampleVo
from src.apis.cell.sample_cell import SampleCell


class SampleService(object):
    __sample_cell: SampleCell

    def __init__(self):
        self.__sample_cell = SampleCell()

    def creation(self, _item: SampleBo, response: Response) -> AssertResponse:
        _result: bool = self.__sample_cell.creation(_item)
        return AssertResponse(_result)

    def deletion(self, _id: int, response: Response) -> AssertResponse:
        _result: bool = self.__sample_cell.deletion(_id)
        return AssertResponse(_result)

    def modify(self, _item: SampleBo, response: Response) -> AssertResponse:
        _result: bool = self.__sample_cell.modify(_item)
        return AssertResponse(_result)

    def detail(self, _id: int, response: Response) -> Optional[SampleVo]:
        data: SampleVo = self.__sample_cell.detail(_id)
        if data is not None:
            return data
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return None

    def page(self, keyword: str, page_num: int, page_size: int, response: Response) -> Page:
        return self.__sample_cell.page(keyword, page_num, page_size)

    def crawler_json(self, _page: int, _size: int, response: Response) -> AssertResponse:
        self.__sample_cell.async_crawler_json(_page, _size)
        return AssertResponse()

    def crawler_html(self, _id: str, response: Response) -> AssertResponse:
        self.__sample_cell.async_crawler_html(_id)
        return AssertResponse()
