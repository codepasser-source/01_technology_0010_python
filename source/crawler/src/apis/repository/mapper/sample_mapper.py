#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/11
from typing import Optional

from src.configuration import SqlMapper, SqlTemplate, RowBound, Page
from src.apis.model import SampleBo, SampleVo


class SampleMapper(object):
    sql_template: SqlTemplate

    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_template = SqlTemplate()
        self.sql_mapper = SqlMapper()

    def creation(self, _item: SampleBo) -> int:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_CREATION'})
        _result: int = self.sql_mapper.insert(sql_id, params=dict(_item))
        return _result

    def deletion(self, _id: int) -> int:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DELETION'})
        _result: int = self.sql_mapper.delete(sql_id, params={"id": _id})
        return _result

    def modify(self, _item: SampleBo) -> int:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_UPDATE'})
        _result: int = self.sql_mapper.update(sql_id, params=dict(_item))
        return _result

    def detail(self, _id: int) -> Optional[SampleVo]:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DETAIL'})
        params = {'id': _id}
        data = self.sql_mapper.select_one(sql_id, params=params)

        if data:
            data.update({'create_time': data.pop('create_time').strftime("%Y-%m-%d %H:%M:%S")})
            data.update({'update_time': data.pop('update_time').strftime("%Y-%m-%d %H:%M:%S")})
            return SampleVo(data)
        else:
            return None

    def page(self, keyword: str, page_num: int, page_size: int) -> Page:
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
