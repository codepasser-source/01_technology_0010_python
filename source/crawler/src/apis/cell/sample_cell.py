#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/11
from typing import Optional
from pyquery import PyQuery as pq

from src.configuration import Page, ConfigLogger, ConfigAppYaml, AsyncCaller, PropsDataType, PropsCharset, PropsVar
from src.common.utils.request import Request
from src.common import Variables, get_timestamp
from src.apis.model import SampleBo, SampleVo
from src.apis.repository.mapper.sample_mapper import SampleMapper

SYSTEM_LOGGER = ConfigLogger.system_log()


class SampleCell(object):
    __sample_mapper: SampleMapper

    def __init__(self):
        self.__sample_mapper = SampleMapper()

    def creation(self, _item: SampleBo) -> bool:
        _result: int = self.__sample_mapper.creation(_item)
        return _result > 0

    def deletion(self, _id: int) -> bool:
        _result: int = self.__sample_mapper.deletion(_id)
        return _result > 0

    def modify(self, _item: SampleBo) -> bool:
        _result: int = self.__sample_mapper.modify(_item)
        return _result > 0

    def detail(self, _id: int) -> Optional[SampleVo]:
        data: SampleVo = self.__sample_mapper.detail(_id)
        if data is not None:
            return data
        else:
            return None

    def page(self, keyword: str, page_num: int, page_size: int) -> Page:
        return self.__sample_mapper.page(keyword, page_num, page_size)

    @AsyncCaller
    def async_crawler_json(self, _page: int, _size: int):
        _api = ConfigAppYaml().sample_json_api()
        _var: dict = {PropsVar.PAGE.key: _page, PropsVar.SIZE.key: _size, PropsVar.TIMESTAMP.key: get_timestamp(True)}
        _params = {'page': '%(page)s', 'size': '%(size)s', 'timestamp': '%(timestamp)s'}
        _payload = {}

        _params = Variables.dict_replace(_params, _var)
        _payload = Variables.dict_replace(_payload, _var)
        _config = {
            'cookies': {'a': '1'},
            'headers': {'b': '2'}
        }
        SYSTEM_LOGGER.info('SampleCell [REQU] async_crawler_json -> [params:%(params)s], [payload:%(payload)s]' % {'params': _params, 'payload': _payload})
        _s_timestamp = get_timestamp(True)
        _resp = Request(_api).post(params=_params, data=_payload, kwargs=_config)
        _e_timestamp = get_timestamp(True)
        _total = _resp['totalElements']
        SYSTEM_LOGGER.info('SampleCell [RESP] async_crawler_json -> [total:%(total)s]' % {'total': _total})

    @AsyncCaller
    def async_crawler_html(self, _id: str):
        _api = ConfigAppYaml().sample_html_api()
        _var = {PropsVar.ID.key: _id}
        _api = Variables.replace(_api, _var)
        _var = {PropsVar.TIMESTAMP.key: get_timestamp(True)}
        _params = {'timestamp': '%(timestamp)s'}

        _params = Variables.dict_replace(_params, _var)
        _config = {
            'cookies': {'a': '1'},
            'headers': {'b': '2'}
        }
        SYSTEM_LOGGER.info('SampleCell [REQU] async_crawler_html -> [params:%(params)s]' % {'params': _params})
        _s_timestamp = get_timestamp(True)
        _resp = Request(_api).get(data_type=PropsDataType.HTML, data_charset=PropsCharset.UTF8, params=_params, kwargs=_config)

        _doc = pq(_resp)
        _tables = _doc.find('div.section div.table-response table.table')
        _position = 0
        _row = 0
        _col = 0
        _table = _tables[_position]
        _trs = pq(_table).find('tbody tr')
        _tr = _trs[_row]
        _tds = pq(_tr).find('td')
        _td = _tds[_col]

        _label = pq(_td).text()

        _e_timestamp = get_timestamp(True)
        SYSTEM_LOGGER.info('SampleCell [RESP] async_crawler_html -> [label:%(label)s]' % {'label': _label})
