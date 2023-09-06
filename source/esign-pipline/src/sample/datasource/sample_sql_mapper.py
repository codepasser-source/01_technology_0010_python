#!/usr/bin/python3
# file name: sample_sql_mapper.py
# author: codepasser
# date: 2022/9/21
import time

from src.configuration import SqlMapper


class SampleSqlMapper:
    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_mapper = SqlMapper()

    def basic(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_BASIC'})
        params = {'age': 4.3}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def include(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_INCLUDE'})
        params = {'age': 4.3}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def logic_if(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_LOGIC_IF'})
        params = {'age': 4.3}
        print(self.sql_mapper.select_one(sql_id, params=params))

    def logic_choose(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_LOGIC_CHOOSE'})
        params = {'name': '乐乐', 'age': 4}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def logic_foreach(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_LOGIC_FOREACH'})
        params = {'names': ['乐乐', '嗯呐', '周周']}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def trim(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_TRIM'})
        print(self.sql_mapper.select_one(sql_id))

    def where(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_WHERE'})
        params = {'age': 4}
        print(self.sql_mapper.select_one(sql_id, params=params))

    def like(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_LIKE'})
        params = {'name': '乐乐'}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def func(self):
        create_time = time.localtime()
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_FUNCTION'})
        params = {'name': '乐乐', 'create_time': create_time}
        print(self.sql_mapper.select_list(sql_id, params=params))

    def insert(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_INSERT'})
        params = {'name': '乐乐', 'age': 4}
        print(self.sql_mapper.insert(sql_id, params=params))

    def insert_multi(self):
        update_time = time.localtime()
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_INSERT_MULTI'})
        params = {'items': [
            {'name': '乐乐', 'age': 4, 'update_time': update_time},
            {'name': '嗯呐', 'age': 4, 'update_time': update_time},
            {'name': '周周', 'age': 4, 'update_time': update_time},
        ]}
        print(self.sql_mapper.insert(sql_id, params=params))

    def update(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_UPDATE'})
        params = {'name': '乐乐', 'age': 5}
        print(self.sql_mapper.update(sql_id, params=params))

    def delete(self):
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_SAMPLE', 'id': 'SAMPLE_DELETE'})
        params = {'id': 1}
        print(self.sql_mapper.delete(sql_id, params=params))


sample = SampleSqlMapper()

# sample.basic()
# sample.include()
# sample.logic_if()
# sample.logic_choose()
# sample.logic_foreach()
# sample.trim()
# sample.where()
# sample.like()
# sample.func()
# sample.insert()
# sample.insert_multi()
# sample.update()
sample.delete()
