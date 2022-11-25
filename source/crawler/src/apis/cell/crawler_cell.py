#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2022/11/15
from src.configuration import ConfigLogger, ConfigAppIni, PropsVar
from src.configuration import CrawlerSettings as Settings

from src.apis.cell.crawler.crawler_handler import CrawlerHandler

SYSTEM_LOGGER = ConfigLogger.system_log()


class CrawlerCell(object):
    __crawler_handler: CrawlerHandler

    def process(self, _setting: dict):
        self.__crawler_handler = CrawlerHandler(_setting)
        _pagination = _setting.get(Settings.PAGINATION.key)

        if _pagination:
            # CRAWLER PAGINATION
            self.__crawler_handler.pagination()
        else:
            # TODO CRAWLER DETAIL
            print('CRAWLER DETAIL')
