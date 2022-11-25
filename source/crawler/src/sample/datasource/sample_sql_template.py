#!/usr/bin/python3
# file name: sample_sql_template.py
# author: codepasser
# date: 2022/9/20
from src.configuration import SqlTemplate, RowBound, Page
from src.common import get_time


def drop_table_function(connection):
    cursor = connection.cursor()
    try:
        sql = 'DROP TABLE IF EXISTS `sample`'
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        return data
    finally:
        cursor.close()


def create_table_function(connection):
    cursor = connection.cursor()
    try:
        sql = """
        CREATE TABLE `sample` (
            `id` int NOT NULL AUTO_INCREMENT,
            `name` char(10) NOT NULL,
            `age` tinyint NOT NULL,
            `create_time` datetime not null default CURRENT_TIMESTAMP comment '创建时间',
            `update_time` datetime not null default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        return data
    finally:
        cursor.close()


class SampleSqlTemplate:
    sql_template: SqlTemplate

    def __init__(self):
        self.sql_template = SqlTemplate()

    def select_one(self):
        print('============{}============'.format('select_one'))
        print(
            self.sql_template.select_one(sql='select * from sample where id=%s', args=(1))
        )

    def select_list(self):
        print('============{}============'.format('select_with row_bound'))
        print(
            self.sql_template.select_list(
                sql='select * from sample where id in (%s,%s,%s)',
                row_bound=RowBound(page_num=1, page_size=2),
                args=(1, 2, 3)
            )
        )
        print('============{}============'.format('select_only'))
        print(
            self.sql_template.select_list(sql='select * from sample where id in (%s,%s,%s)', args=(1, 2, 3))
        )

    def select_with_no_params(self):
        print('============{}============'.format('select_with_no_params'))
        print(
            self.sql_template.select_one(sql='select * from sample where id=1')
        )

    def select_page(self):
        print('============{}============'.format('select_page'))
        page_data: Page = self.sql_template.select_page(
            sql='select * from sample',
            row_bound=RowBound(page_num=1, page_size=2)
        )
        print(page_data.page_num)
        print(page_data.page_size)
        print(page_data.total)
        print(page_data.list)

    def insert_one(self):
        print('============{}============'.format('insert_one'))
        row = self.sql_template.insert(
            sql='insert into sample(name,age) values(%s,%s)',
            args=('乐乐', 3)
        )
        print(row)

    def insert_multi(self):
        print('============{}============'.format('insert_multi'))
        row = self.sql_template.insert_batch(
            sql='insert into sample(name,age) values(%s,%s)',
            args=(
                ['乐乐', 3],
                ['嗯呐', 3],
                ['周周', 3]
            )
        )
        print(row)

    def insert_dynamic_multi(self):
        print('============{}============'.format('insert_dynamic_multi'))
        _now = get_time()
        _mappings: [str] = ['name', 'age', 'create_time']
        _placeholders: [str] = []
        for _i in range(len(_mappings)):
            _placeholders.append('%s')
        _mappings = ','.join(_mappings)
        _placeholders = ','.join(_placeholders)
        _records: [] = [
            ['乐乐', 3, _now],
            ['嗯呐', 3, _now],
            ['周周', 3, _now]
        ]
        _sql = 'insert into sample({}) values({})'.format(_mappings, _placeholders)
        row = self.sql_template.insert_batch(
            sql=_sql,
            args=_records
        )
        print(row)

    def update(self):
        print('============{}============'.format('update'))
        row = self.sql_template.update(
            sql='update sample set age = %s where id = %s',
            args=(4, 1)
        )
        print(row)

    def delete(self):
        print('============{}============'.format('delete'))
        row = self.sql_template.delete(
            sql='delete from sample where id in(%s,%s,%s)',
            args=(1, 2, 3)
        )
        print(row)

    def drop_in_connection(self):
        print('============{}============'.format('drop_in_connection'))
        print(self.sql_template.execute_in_connection(drop_table_function))

    def create_in_connection(self):
        print('============{}============'.format('create_in_connection'))
        print(self.sql_template.execute_in_connection(create_table_function))


sample = SampleSqlTemplate()

sample.drop_in_connection()
sample.create_in_connection()
#
# sample.insert_one()
# sample.insert_multi()
sample.insert_dynamic_multi()
#
# sample.select_one()
# sample.select_list()
# sample.select_with_no_params()
# sample.select_page()
# sample.select_list()
# sample.update()
# sample.select_list()
# sample.delete()
# sample.select_list()
