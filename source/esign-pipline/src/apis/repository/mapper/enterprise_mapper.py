#!/usr/bin/python3
# file name: sample_mapper.py
# author: codepasser
# date: 2023/9/7
from typing import Optional

from src.configuration import ConfigLogger, SqlMapper, SqlTemplate, RowBound, Page

SYSTEM_LOGGER = ConfigLogger.system_log()


class EnterpriseMapper:
    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_mapper = SqlMapper()

    def page(self, page: int, size: int) -> Page:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_QX', 'id': 'QX_ENTERPRISE_FULL'})
        params = {}

        page_data: Page = self.sql_mapper.select_page(
            sql_id,
            params=params,
            row_bound=RowBound(page=page, size=size)
        )
        return page_data
