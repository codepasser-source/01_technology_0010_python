#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/9/21
from typing import Optional
from fastapi import HTTPException

from src.configuration import ConfigLogger, Page
from src.apis.model import AssertResponse, SampleBo, SampleVo
from src.apis.repository.mapper.sample_mapper import SampleMapper

CONSOLE_LOGGER = ConfigLogger.console_log()


class SampleService(object):
    sample_mapper: SampleMapper

    def __init__(self):
        self.sample_mapper = SampleMapper();

    def creation(self, _item: SampleBo) -> AssertResponse:
        CONSOLE_LOGGER.info(_item)
        self.sample_mapper.creation(_item)
        return AssertResponse()

    def deletion(self, _id: int) -> AssertResponse:
        CONSOLE_LOGGER.info(_id)
        count: int = self.sample_mapper.deletion(_id)
        if count == 0:
            raise HTTPException(status_code=404, detail="data not found")

        return AssertResponse()

    def modify(self, _item: SampleBo) -> AssertResponse:
        CONSOLE_LOGGER.info(_item)
        count: int = self.sample_mapper.modify(_item)
        if count == 0:
            raise HTTPException(status_code=404, detail="data not found")

        return AssertResponse()

    def detail(self, _id: int) -> Optional[SampleVo]:
        CONSOLE_LOGGER.info(_id)
        data = self.sample_mapper.detail(_id)
        if data is None:
            raise HTTPException(status_code=404, detail="data not found")

        data.update({'create_time': data.pop('create_time').strftime("%Y-%m-%d %H:%M:%S")})
        data.update({'update_time': data.pop('update_time').strftime("%Y-%m-%d %H:%M:%S")})

        vo: SampleVo = SampleVo()
        for key, value in data.items():
            setattr(vo, key, value)
        return vo

    def page(self, keyword: str, page: int, size: int) -> Page:
        CONSOLE_LOGGER.info('page_num:{} page_size{}'.format(page, size))
        return self.sample_mapper.page(keyword, page, size)
