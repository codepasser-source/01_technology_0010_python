#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/9/21
from typing import Optional

from fastapi import HTTPException
from src.configuration import ConfigLogger, SqlMapper, SqlTemplate, RowBound, Page
from src.apis.model import AssertResponse, SampleBo, SampleVo

CONSOLE_LOGGER = ConfigLogger.console_log()


class SampleService(object):
    sql_template: SqlTemplate

    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_template = SqlTemplate()
        self.sql_mapper = SqlMapper()

    def creation(self, _item: SampleBo):
        CONSOLE_LOGGER.info(_item)
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_CREATION'})
        self.sql_mapper.insert(sql_id, params=dict(_item))
        return AssertResponse()

    def deletion(self, _id: int):
        CONSOLE_LOGGER.info(_id)
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DELETION'})
        count = self.sql_mapper.delete(sql_id, params={"id": _id})
        if count == 1:
            return AssertResponse()
        else:
            raise HTTPException(status_code=404, detail="data not found")

    def modify(self, _item: SampleBo):
        CONSOLE_LOGGER.info(_item)
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_UPDATE'})
        count = self.sql_mapper.update(sql_id, params=dict(_item))
        if count == 1:
            return AssertResponse()
        else:
            raise HTTPException(status_code=404, detail="data not found")

    def detail(self, _id: int) -> Optional[SampleVo]:
        CONSOLE_LOGGER.info(_id)
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DETAIL'})
        params = {'id': _id}
        data = self.sql_mapper.select_one(sql_id, params=params)
        if data:
            data.update({'create_time': data.pop('create_time').strftime("%Y-%m-%d %H:%M:%S")})
            data.update({'update_time': data.pop('update_time').strftime("%Y-%m-%d %H:%M:%S")})
            vo: SampleVo = SampleVo()
            for key, value in data.items():
                setattr(vo, key, value)
            return vo
        else:
            raise HTTPException(status_code=404, detail="data not found")

    def page(self, keyword: str, page_num: int, page_size: int):
        CONSOLE_LOGGER.info('page_num:{} page_size{}'.format(page_num, page_size))
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_PAGE'})
        params = {}
        if keyword:
            params = {'keyword': keyword}
        page_data: Page = self.sql_mapper.select_page(
            sql_id,
            params=params,
            row_bound=RowBound(page_num=page_num, page_size=page_size)
        )
        return page_data
