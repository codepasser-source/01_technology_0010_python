#!/usr/bin/python3
# file name: app_router.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body, Response
from typing import Union, Optional, List

from src.apis.model import AssertResponse


class AppDebugRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/crawler-api/debug",
                    tags=['CRAWLER-APIS : 【AppDebugRouter】'],
                    summary='【AppDebugRouter】调试服务',
                    description='【AppDebugRouter】调试服务',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def root():
            return AssertResponse()

    def config(self):
        return self.__router
