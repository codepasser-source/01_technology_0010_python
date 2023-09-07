#!/usr/bin/python3
# file name: router.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body
from typing import Optional

from src.configuration import Page
from src.apis.model import AssertResponse, SampleBo, SampleVo

from apis.service.sample_service import SampleService


class AppSampleRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次
    __sample_service: SampleService = SampleService()

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.post(path="/esg-api/sample",
                     tags=['ESIGN-PIPLINE-APIS : SAMPLE'],
                     summary='新增对象',
                     description='新增对象',
                     response_model=AssertResponse,
                     status_code=200)
        async def sample_creation(_item: SampleBo = Body(None, description="request body")):
            return self.__sample_service.creation(_item)

        @router.delete(path="/esg-api/sample/{_id}",
                       tags=['ESIGN-PIPLINE-APIS : SAMPLE'],
                       summary='删除对象',
                       description='删除对象',
                       response_model=AssertResponse,
                       status_code=200)
        async def sample_deletion(_id: int = Path(description="id")):
            return self.__sample_service.deletion(_id)

        @router.put(path="/esg-api/sample",
                    tags=['ESIGN-PIPLINE-APIS : SAMPLE'],
                    summary='更新对象',
                    description='更新对象',
                    response_model=AssertResponse,
                    status_code=200)
        async def sample_modify(_item: SampleBo = Body(None, description="request body")):
            return self.__sample_service.modify(_item)

        @router.get(path="/esg-api/sample/{_id}",
                    tags=['ESIGN-PIPLINE-APIS : SAMPLE'],
                    summary='查询对象',
                    description='查询对象',
                    response_model=Optional[SampleVo],
                    status_code=200)
        async def sample_detail(_id: int = Path(description="id")):
            return self.__sample_service.detail(_id)

        @router.get(path="/esg-api/sample",
                    tags=['ESIGN-PIPLINE-APIS : SAMPLE'],
                    summary='查询分页',
                    description='查询分页',
                    response_model=Page,
                    status_code=200)
        async def sample_page(
                keyword: Optional[str] = Query(None, description="keyword"),
                page: int = Query(1, description="page"),
                size: int = Query(10, description="size")):
            return self.__sample_service.page(keyword, page, size)

    def config(self):
        return self.__router
