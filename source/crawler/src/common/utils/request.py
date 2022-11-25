#!/usr/bin/python3
# author: codepasser
# date: 2022/02/15
import json
import requests

from requests.adapters import HTTPAdapter
from src.configuration import ConfigAppIni, ConfigAppYaml, PropsDataType, PropsCharset, PropsMethod


class Request:
    __user_agent: str = ConfigAppIni().get("app", "user-agent")
    __requ_error: dict = ConfigAppYaml().get_requ_error()
    __resp_error: dict = ConfigAppYaml().get_resp_error()

    def __init__(self, url):
        self.url = url

    def get(self, data_type: PropsDataType = PropsDataType.JSON, data_charset: PropsCharset = None, params=None, **kwargs):
        if params is None:
            params = {}
        _headers = {
            'Accept-Charset': 'utf-8',
            'Content-Type': 'application/json',
            'User-Agent': self.__user_agent
        }
        if 'headers' in kwargs['kwargs']:
            for key, value in kwargs['kwargs'].get('headers').items():
                # print("{0}:{1}".format(key, value))
                _headers[key] = value

        _cookies = {}
        if 'cookies' in kwargs['kwargs']:
            for key, value in kwargs['kwargs'].get('cookies').items():
                # print("{0}:{1}".format(key, value))
                _cookies[key] = value

        _request = requests.Session()
        # 将适配器挂载到session上面
        _request.mount('http://', HTTPAdapter(max_retries=3))
        _request.mount('https://', HTTPAdapter(max_retries=3))
        _response = _request.get(self.url, params=params, headers=_headers, cookies=_cookies, timeout=(50.05, 60.05))

        return self.__handle(_response, data_type, data_charset, PropsMethod.GET)

    def post(self, data_type: PropsDataType = PropsDataType.JSON, data_charset: PropsCharset = None, params=None, data=None, **kwargs):
        if params is None:
            params = {}
        if data is None:
            data = {}
        _headers = {
            'Accept-Charset': 'utf-8',
            'Content-Type': 'application/json',
            'User-Agent': self.__user_agent
        }
        if 'headers' in kwargs['kwargs']:
            for key, value in kwargs['kwargs'].get('headers').items():
                # print("{0}:{1}".format(key, value))
                _headers[key] = value

        _cookies = {}
        if 'cookies' in kwargs['kwargs']:
            for key, value in kwargs['kwargs'].get('cookies').items():
                # print("{0}:{1}".format(key, value))
                _cookies[key] = value

        _request = requests.Session()
        # 将适配器挂载到session上面
        _request.mount('http://', HTTPAdapter(max_retries=3))
        _request.mount('https://', HTTPAdapter(max_retries=3))
        _response = _request.post(self.url, params=params, data=json.dumps(data), headers=_headers, cookies=_cookies, timeout=(50.05, 60.05))
        return self.__handle(_response, data_type, data_charset, PropsMethod.POST)

    def __handle(self, _response, _data_type: PropsDataType = PropsDataType.JSON, data_charset: PropsCharset = None, _method: PropsMethod = PropsMethod.GET):
        _response_status = _response.status_code
        if self.__requ_error.get(_response_status) is not None:
            raise Exception('An error occurred in the [REQUEST {}], [status:{}], [response:{}]'.format(_method.key, _response_status, _response.text))
        if self.__resp_error.get(_response_status) is not None:
            raise Exception('An error occurred in the [RESPONSE {}], [status:{}], [response:{}]'.format(_method.key, _response_status, _response.text))
        try:
            _response_data = _response.text
            if _data_type == PropsDataType.JSON:
                return json.loads(_response_data)
            if _data_type == PropsDataType.HTML:
                if data_charset is not None:
                    _response_data = _response.content
                    return str(_response_data, data_charset.key)
                else:
                    return _response_data
        except Exception as e:
            raise Exception('An error occurred in the [RESPONSE {} HAND], [data_type:{}], [status:{}], [response:{}], [caused by:{}]'.format(_method.key, _data_type, _response_status, _response.text, e))
