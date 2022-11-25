#!/usr/bin/python3
# file name: router_app.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body, Response
from typing import Union, Optional, List
from src.information import ApplicationInfo
from src.configuration import ConfigLogger
from src.apis.model import AssertResponse

CONSOLE_LOGGER = ConfigLogger.console_log()

SYSTEM_LOGGER = ConfigLogger.system_log()

UVICORN_LOGGER = ConfigLogger.uvicorn_log()


class AppRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/crawler-api",
                    tags=['CRAWLER-APIS : 【AppRouter】'],
                    summary='【AppRouter】健康检查',
                    description='【AppRouter】健康检查',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def root():
            CONSOLE_LOGGER.info('console log')
            SYSTEM_LOGGER.info('system log')
            UVICORN_LOGGER.info('uvicorn log')
            return AssertResponse()

        @router.get(path="/crawler-api/info",
                    tags=['CRAWLER-APIS : 【AppRouter】'],
                    summary='【AppRouter】服务信息',
                    description='【AppRouter】服务信息',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def info():
            ApplicationInfo.info()
            return AssertResponse()

    def config(self):
        return self.__router
