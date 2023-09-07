#!/usr/bin/python3
# file name: sample_service.py
# author: codepasser
# date: 2023/9/7
from typing import Optional
from fastapi import HTTPException

from src.configuration import ConfigLogger, Page

from src.apis.repository.mapper.enterprise_mapper import EnterpriseMapper

CONSOLE_LOGGER = ConfigLogger.console_log()


class EnterpriseService(object):
    enterprise_mapper: EnterpriseMapper

    def __init__(self):
        self.enterprise_mapper = EnterpriseMapper()

    def page(self, page: int, size: int) -> Page:
        CONSOLE_LOGGER.info('page:{} size{}'.format(page, size))
        return self.enterprise_mapper.page(page, size)
