#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/15
from typing import List

from src.configuration import ConfigLogger, ConfigAppIni, PropsVar, PropsMethod, PropsDataType, PropsConvertType
from src.configuration import CrawlerSettings as Settings
from src.common import Variables, Dicts, Paper, get_timestamp, convert_time
from src.common.utils.request import Request

from src.apis.cell.crawler.crawler_template import CrawlerTemplate

SYSTEM_LOGGER = ConfigLogger.system_log()

CONSOLE_LOGGER = ConfigLogger.console_log()


class CrawlerHandler(object):
    __title: str
    __url: str
    __method: str
    __data_type: str
    __pagination: bool
    __pagination_page: int
    __pagination_size: int
    __params: dict
    __payload: dict
    __data_mapper: str
    __data_total_mapper: str
    __data_convert: dict
    __db_table: str
    __db_mapping: dict

    __timestamp_convert: dict  # 动态类型转换
    __mappings: List[str]  # 动态SQL:列映射

    def __init__(self, _setting: dict):
        self.__title = _setting.get(Settings.TITLE.key)
        self.__url = _setting.get(Settings.URL.key)
        self.__method = _setting.get(Settings.METHOD.key)
        self.__data_type = _setting.get(Settings.DATA_TYPE.key)
        self.__pagination = _setting.get(Settings.PAGINATION.key)
        self.__pagination_page = _setting.get(Settings.PAGINATION_PAGE.key)
        self.__pagination_size = _setting.get(Settings.PAGINATION_SIZE.key)
        self.__params = _setting.get(Settings.PARAMS.key)
        self.__payload = _setting.get(Settings.PAYLOAD.key)
        self.__data_mapper = _setting.get(Settings.DATA_MAPPER.key)
        self.__data_total_mapper = _setting.get(Settings.DATA_TOTAL_MAPPER.key)
        self.__data_convert = _setting.get(Settings.DATA_CONVERT.key)
        self.__db_table = _setting.get(Settings.DB_TABLE.key)
        self.__db_mapping = _setting.get(Settings.DB_MAPPING.key)
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [title:{}]'.format(self.__title))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [url:{}]'.format(self.__url))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [method:{}]'.format(self.__method))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [data_type:{}]'.format(self.__data_type))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [pagination:{}]'.format(self.__pagination))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [pagination_page:{}]'.format(self.__pagination_page))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [pagination_size:{}]'.format(self.__pagination_size))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [params:{}]'.format(self.__params))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [payload:{}]'.format(self.__payload))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [data_mapper:{}]'.format(self.__data_mapper))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [data_total_mapper:{}]'.format(self.__data_total_mapper))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [data_convert:{}]'.format(self.__data_convert))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [db_table:{}]'.format(self.__db_table))
        SYSTEM_LOGGER.info('TASK - [SETTING] -> [db_mapping:{}]'.format(self.__db_mapping))

        # 解析类型转换 TODO CONVERT TYPE
        self.__timestamp_convert = self.__data_convert.get(PropsConvertType.TIMESTAMP.key)

        # 解析列
        _mappings: [str] = []
        for _key in self.__db_mapping.keys():
            _mappings.append(self.__db_mapping.get(_key))
        self.__mappings = _mappings

    def pagination(self):
        _limit = int(ConfigAppIni().get('poi', 'limit'))
        _last: bool = False
        _cursor: int = 1  # 当前游标
        _page: int = self.__pagination_page
        _size: int = self.__pagination_size

        _ts_timestamp = get_timestamp(True)
        SYSTEM_LOGGER.info('HAND - [TASK] - [STARTED] -> [title:{}], [limit:{}]'.format(self.__title, _limit))
        while (_limit == 0 or _cursor <= _limit) and (_last is not True):
            _s_timestamp = get_timestamp(True)
            SYSTEM_LOGGER.info('HAND - [PAGINATION] - [STARTED] -> [cursor:{}], [limit:{}]'.format(_cursor, _limit))
            _var: dict = {PropsVar.PAGE.key: _page, PropsVar.SIZE.key: _size, PropsVar.TIMESTAMP.key: get_timestamp(True)}
            _url: str = Variables.replace(self.__url, _var)
            _params: dict = Variables.dict_replace(self.__params, _var)
            _payload: dict = Variables.dict_replace(self.__payload, _var)
            _last = self._require_pagination(_url, _params, _payload, _cursor, _size)
            _e_timestamp = get_timestamp(True)
            SYSTEM_LOGGER.info('HAND - [PAGINATION] - [COMPLETED] -> [cursor:{}], [limit:{}], [timer:{}S]'.format(_cursor, _limit, round(_e_timestamp - _s_timestamp, 2)))

            _cursor += 1
            _page += 1
        # outside while
        _te_timestamp = get_timestamp(True)
        SYSTEM_LOGGER.info('HAND - [TASK] - [COMPLETED] -> [title:{}], [limit:{}], [timer:{}S]'.format(self.__title, _limit, round(_te_timestamp - _ts_timestamp, 2)))

    def _require_pagination(self, _url: str, _params: dict, _payload: dict, _cursor: int, _size: int) -> bool:
        _last: bool = True
        _timestamp = get_timestamp(True)
        _config: dict = {}
        SYSTEM_LOGGER.info('HAND - [PAGINATION] - [REQU] -> [cursor:{}], [url:{}], [params:{}], [payload:{}]'.format(_cursor, _url, _params, _payload))
        _s_timestamp = get_timestamp(True)

        _response: dict = {}
        # TODO DATA_TYPE
        if self.__method == PropsMethod.GET.value:
            _response = Request(_url).get(params=_params, kwargs=_config)
        if self.__method == PropsMethod.POST.value:
            _response = Request(_url).post(params=_params, data=_payload, kwargs=_config)

        _e_timestamp = get_timestamp(True)

        _data = Dicts.dict_mapper(_response, self.__data_mapper)

        _total = Dicts.dict_mapper(_response, self.__data_total_mapper)

        _total_page = Paper(_total, self.__pagination_size).total_page()

        _count = len(_data)

        SYSTEM_LOGGER.info('HAND - [PAGINATION] - [RESP] -> [cursor:{}], [total:{}], [total_page:{}], [count:{}]'.format(_cursor, _total, _total_page, _count))

        self.__multi_handle(_data)

        _last = (_total is None or (_cursor >= _total_page))
        return _last

    def __multi_handle(self, _data: List[dict]):
        if _data is None:
            return
        # 数据集合
        _records: List[List] = []  # 动态SQL:值映射
        for _i in range(len(_data)):
            _record: List = []
            _item: dict = _data.__getitem__(_i)
            # 解析值
            for _key in self.__db_mapping.keys():
                _value = self.__convert_value(_key, _item.get(_key))
                _record.append(_value)
            # outside inner for
            _records.append(_record)
        # outside for
        CONSOLE_LOGGER.debug('HAND - [MULTI] -> [table:{}], [mappings:{}], [records:{}]'.format(self.__db_table, self.__mappings, _records))
        if len(_records) > 0:
            CrawlerTemplate().dynamic_multi_save(self.__db_table, self.__mappings, _records)

    def __convert_value(self, _mapping: str, _value: any):
        _val: any = _value

        if self.__timestamp_convert is not None:
            _found = self.__timestamp_convert.get(_mapping)
            if _found is not None:
                if _found == PropsConvertType.SECOND.value:
                    _val = convert_time(_value)
                if _found == PropsConvertType.MILLISECOND.value:
                    _val = convert_time(int(_value / 1000))

        return _val
