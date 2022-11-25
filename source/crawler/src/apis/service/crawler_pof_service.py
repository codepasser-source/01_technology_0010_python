#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/15
from typing import List

from fastapi import Response

from src.configuration import AsyncCaller, ConfigLogger, ConfigCrawlerYaml, ConfigCrawlerPOFYaml
from src.common import get_timestamp

from src.apis.model import AssertResponse
from src.apis.cell.crawler_cell import CrawlerCell

SYSTEM_LOGGER = ConfigLogger.system_log()


class CrawlerPOFService(object):
    __settings: ConfigCrawlerYaml

    def __init__(self):
        self.__settings = ConfigCrawlerPOFYaml()

    def start(self, response: Response) -> AssertResponse:
        self.__start()
        return AssertResponse()

    @AsyncCaller
    def __start(self):
        _title: str = self.__settings.title()
        _tasks: List[str] = self.__settings.get_task()
        if _tasks is None or len(_tasks) == 0:
            SYSTEM_LOGGER.warning('No tasks can be started -> [title:{}], [tasks:{}]'.format(_title, _tasks))
            return

        SYSTEM_LOGGER.info('TASK - [STARTED] -> [title:{}], [tasks:{}]'.format(_title, _tasks))
        _s_timestamp = get_timestamp(True)
        for _i in range(len(_tasks)):
            _task = _tasks[_i]
            _setting = self.__settings.get_task(_task)
            if _setting is not None:
                try:
                    CrawlerCell().process(_setting)
                except Exception as e:
                    SYSTEM_LOGGER.error('TASK - [ERROR] -> [title:{}], [error:{}]'.format(_title, e))

        # outside for
        _e_timestamp = get_timestamp(True)
        SYSTEM_LOGGER.info('TASK - [COMPLETED] -> [title:{}], [timer:{}S]'.format(_title, round(_e_timestamp - _s_timestamp, 2)))
