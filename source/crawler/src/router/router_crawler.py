#!/usr/bin/python3
# file name: router_amac.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body, Response
from typing import Union, Optional, List

from src.configuration import ConfigLogger, ConfigCrawlerPOFYaml
from src.apis.model import AssertResponse
from src.apis.service.crawler_pof_service import CrawlerPOFService

SYSTEM_LOGGER = ConfigLogger.system_log()


class AppCrawlerRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次
    __crawler_pof_service: CrawlerPOFService = CrawlerPOFService()

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/crawler-api/crawler",
                    tags=['CRAWLER-APIS : 【AppCrawlerRouter】'],
                    summary='【AppCrawlerRouter】爬虫服务',
                    description='【AppCrawlerRouter】爬虫服务',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def root():
            _config = ConfigCrawlerPOFYaml()
            _tasks: List[str] = _config.get_task()
            SYSTEM_LOGGER.info(_tasks)
            for _i in range(len(_tasks)):
                _task = _tasks[_i]
                SYSTEM_LOGGER.info(_config.get_task(_task))

            return AssertResponse()

        @router.get(path="/crawler-api/crawler/pof",
                    tags=['CRAWLER-APIS : 【AppCrawlerRouter】'],
                    summary='【AppCrawlerRouter】【AMAC】私募基金相关机构公示信息 爬虫启动',
                    description='【AppCrawlerRouter】【AMAC】私募基金相关机构公示信息 爬虫启动',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def crawler_pof(response: Response = None):
            return self.__crawler_pof_service.start(response)

    def config(self):
        return self.__router
