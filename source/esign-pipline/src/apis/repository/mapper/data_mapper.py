#!/usr/bin/python3
# file name: data_mapper.py
# author: codepasser
# date: 2022/9/21
import time

from typing import List
from src.configuration import ConfigLogger, SqlMapper

SYSTEM_LOGGER = ConfigLogger.system_log()


class DataMapper:
    sql_mapper: SqlMapper

    def __init__(self):
        self.sql_mapper = SqlMapper()

    def data_companies(self, _template_no: str, _year: str, _report: str, _company_code: str = None) -> List[dict]:
        """
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_COMPANIES'})
        params: dict = {
            'ERC_TEMPLATE_NO': _template_no,
            'ERC_YEAR': _year,
            'ERC_REPORT': _report
        }
        if _company_code is not None:
            params['ERC_COMPANY_CODE'] = _company_code
        _data: List[dict] = self.sql_mapper.select_list(sql_id, params=params)
        return _data

    def data_values(self,
                    _template_no: str,
                    _year: str,
                    _report: str,
                    _form: str,
                    _code: str,
                    _handle_id: str = None,
                    _company_code: str = None,
                    _industry_code: str = None) -> List[dict]:
        """
        模版-报告期-公司-指标 -> 数据项-数据值
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_VALUES'})
        params: dict = {
            'ERC_TEMPLATE_NO': _template_no,
            'ERC_YEAR': _year,
            'ERC_REPORT': _report,
            'ERH_FORM': _form,
            'ERTT_CODE': _code,
        }
        if _handle_id is not None:
            # 指标形态为 填空 3|4 时为必须参数（最后评分数据项）
            params['ERCE_HANDLE_ID'] = _handle_id
        if _company_code is not None:
            params['ERC_COMPANY_CODE'] = _company_code
        if _industry_code is not None:
            params['ERC_INDUSTRY_GICS_CODE'] = _industry_code
        _data: List[dict] = self.sql_mapper.select_list(sql_id, params=params)
        return _data

    def data_values_general(self,
                            _template_no: str,
                            _year: str,
                            _report: str,
                            _form: str,
                            _code: str,
                            _handle_id: str) -> List[dict]:
        """
        模版-报告期-公司-指标-通用行业 -> 数据项-数据值
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_VALUES_GENERAL'})
        params: dict = {
            'ERC_TEMPLATE_NO': _template_no,
            'ERC_YEAR': _year,
            'ERC_REPORT': _report,
            'ERH_FORM': _form,
            'ERTT_CODE': _code,
            'ERCE_HANDLE_ID': _handle_id  # 指标形态为 填空 3|4 必须参数（最后评分数据项）
        }
        _data: List[dict] = self.sql_mapper.select_list(sql_id, params=params)
        return _data

    def data_values_industry(self,
                             _template_no: str,
                             _year: str,
                             _report: str,
                             _form: str,
                             _code: str,
                             _handle_id: str) -> List[dict]:
        """
        模版-报告期-公司-指标-特定行业 -> 数据项-数据值
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_VALUES_INDUSTRY'})
        params: dict = {
            'ERC_TEMPLATE_NO': _template_no,
            'ERC_YEAR': _year,
            'ERC_REPORT': _report,
            'ERH_FORM': _form,
            'ERTT_CODE': _code,
            'ERCE_HANDLE_ID': _handle_id  # 指标形态为 填空 3|4 必须参数（最后评分数据项）
        }
        _data: List[dict] = self.sql_mapper.select_list(sql_id, params=params)
        return _data

    def data_hierarchy(self,
                       _scheme_id: str,
                       _template_no: str,
                       _year: str,
                       _report: str,
                       _codes: List[str]) -> List[dict]:
        """
        模版-报告期-公司-指标-特定行业 -> 数据项-数据值
        """
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_HIERARCHY'})
        params: dict = {
            'SCHEME_ID': _scheme_id,
            'TEMPLATE_NO': _template_no,
            'YEAR': _year,
            'REPORT': _report,
            'CODES': _codes
        }
        _data: List[dict] = self.sql_mapper.select_list(sql_id, params=params)
        return _data

    def data_score_clear(self, _scheme_id: str, _template_no: str, _code: str = None) -> int:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_SCORE_CLEAR'})
        params = {
            'SCHEME_ID': _scheme_id,
            'TEMPLATE_NO': _template_no
        }
        if _code is not None:
            params['RATINGS_CODE'] = _code
        _count = self.sql_mapper.delete(sql_id, params=params)
        return _count

    def data_score_save(self, _items: List[dict]) -> int:
        sql_id = ('%(namespace)s.%(id)s' % {'namespace': 'NS_MAPPER_DATA', 'id': 'DATA_SCORE_SAVE'})
        params = {'items': _items}
        _count = self.sql_mapper.insert(sql_id, params=params)
        return _count
