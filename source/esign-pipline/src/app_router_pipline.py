#!/usr/bin/python3
# file name: router.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body
from typing import Optional

from src.configuration import Page
from src.apis.model import AssertResponse, SampleBo, SampleVo

from apis.service.enterprise_service import EnterpriseService


class AppPiplineRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次
    __enterprise_service: EnterpriseService = EnterpriseService()

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/esg-api/pipline",
                    tags=['ESIGN-PIPLINE-APIS : PIPLINE'],
                    summary='企业信息分页查询',
                    description='【启信宝】',
                    response_model=Page,
                    status_code=200)
        async def sample_page(
                page: int = Query(1, description="page"),
                size: int = Query(10, description="size")):
            return self.__enterprise_service.page(page, size)

    def config(self):
        return self.__router
