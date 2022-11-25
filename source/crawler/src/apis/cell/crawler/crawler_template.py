#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/15
from typing import List

from src.configuration import SqlTemplate


class CrawlerTemplate(object):
    sql_template: SqlTemplate

    def __init__(self):
        self.sql_template = SqlTemplate()

    def dynamic_multi_save(self, _db_table, _mappings: List[str], _records: List[List]):
        _placeholders: [str] = []
        for _i in range(len(_mappings)):
            _placeholders.append('%s')
        _columns: str = ','.join(_mappings)
        _placeholders = ','.join(_placeholders)
        _sql = 'INSERT INTO {}({}) VALUES({})'.format(_db_table, _columns, _placeholders)
        _count = self.sql_template.insert_batch(
            sql=_sql,
            args=_records
        )
