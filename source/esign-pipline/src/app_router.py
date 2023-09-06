#!/usr/bin/python3
# file name: app_router.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter
from src.information import ApplicationInfo
from src.configuration import ConfigLogger
from src.apis.model import AssertResponse

SYSTEM_LOGGER = ConfigLogger.system_log()

CONSOLE_LOGGER = ConfigLogger.console_log()

UVICORN_LOGGER = ConfigLogger.uvicorn_log()


class AppRouter:
    __router: APIRouter = None

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/esg-api",
                    tags=['ESIGN-PIPLINE-APIS : DEVOPS'],
                    summary='根路径',
                    description='健康检查',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def root():
            SYSTEM_LOGGER.info('system log')
            CONSOLE_LOGGER.info('console log')
            UVICORN_LOGGER.info('uvicorn log')
            return AssertResponse()

        @router.get(path="/esg-api/info",
                    tags=['ESIGN-PIPLINE-APIS : DEVOPS'],
                    summary='服务信息',
                    description='服务信息',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def info():
            ApplicationInfo.info()
            return AssertResponse()

    def config(self):
        return self.__router
