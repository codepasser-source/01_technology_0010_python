#!/usr/bin/python3
# file name: sample_mapper.py
# author: codepasser
# date: 2022/9/21
from typing import Optional

from src.apis.model.bo.sample_bo import SampleBo
from src.configuration import ConfigLogger, SqlMapper, SqlTemplate, RowBound, Page

SYSTEM_LOGGER = ConfigLogger.system_log()


class SampleMapper:
    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_mapper = SqlMapper()

    def creation(self, _item: SampleBo) -> int:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_CREATION'})
        return self.sql_mapper.insert(sql_id, params=dict(_item))

    def deletion(self, _id: int) -> int:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DELETION'})
        return self.sql_mapper.delete(sql_id, params={"id": _id})

    def modify(self, _item: SampleBo) -> int:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_UPDATE'})
        return self.sql_mapper.update(sql_id, params=dict(_item))

    def detail(self, _id: int) -> Optional[dict]:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_DETAIL'})
        params = {'id': _id}
        return self.sql_mapper.select_one(sql_id, params=params)

    def page(self, keyword: str, page: int, size: int) -> Page:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_SERVICE_PAGE'})
        params = {}
        if keyword:
            params = {'keyword': keyword}

        page_data: Page = self.sql_mapper.select_page(
            sql_id,
            params=params,
            row_bound=RowBound(page=page, size=size)
        )
        return page_data
