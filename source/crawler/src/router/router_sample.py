#!/usr/bin/python3
# file name: router_sample.py
# author: codepasser
# date: 2022/9/9

from fastapi import APIRouter, Query, Path, Body, Response
from typing import Union, Optional, List

from src.configuration import Page

from src.apis.model import AssertResponse, SampleBo, SampleVo

from src.apis.service.sample_service import SampleService


class AppSampleRouter:
    __router: APIRouter = None

    # 注意加载时机，__init__ 重复执行2次
    __sample_service: SampleService = SampleService()

    # 定义构造方法
    def __init__(self):
        router = APIRouter()
        self.__router = router

        @router.get(path="/crawler-api/sample",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】示例服务',
                    description='【AppSampleRouter】示例服务',
                    response_model=AssertResponse,
                    status_code=200
                    )
        async def root():
            return AssertResponse()

        @router.post(path="/crawler-api/sample/mybatis",
                     tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                     summary='【AppSampleRouter】新增对象',
                     description='【AppSampleRouter】新增对象',
                     response_model=AssertResponse,
                     status_code=200)
        async def sample_creation(_item: SampleBo = Body(None, description="request body"), response: Response = None):
            return self.__sample_service.creation(_item, response)

        @router.delete(path="/crawler-api/sample/mybatis/{_id}",
                       tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                       summary='【AppSampleRouter】删除对象',
                       description='【AppSampleRouter】删除对象',
                       response_model=AssertResponse,
                       status_code=200)
        async def sample_deletion(_id: int = Path(description="id"), response: Response = None):
            return self.__sample_service.deletion(_id, response)

        @router.put(path="/crawler-api/sample/mybatis",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】更新对象',
                    description='【AppSampleRouter】更新对象',
                    response_model=AssertResponse,
                    status_code=200)
        async def sample_modify(_item: SampleBo = Body(None, description="request body"), response: Response = None):
            return self.__sample_service.modify(_item, response)

        @router.get(path="/crawler-api/sample/mybatis/{_id}",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】查询对象',
                    description='【AppSampleRouter】查询对象',
                    response_model=Optional[SampleVo],
                    status_code=200)
        async def sample_detail(_id: int = Path(description="id"), response: Response = None):
            return self.__sample_service.detail(_id, response)

        @router.get(path="/crawler-api/sample/mybatis",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】查询分页',
                    description='【AppSampleRouter】查询分页',
                    response_model=Page,
                    status_code=200)
        async def sample_page(
                keyword: Optional[str] = Query(None, description="keyword"),
                page_num: int = Query(1, description="page_num"),
                page_size: int = Query(10, description="page_size"),
                response: Response = None):
            return self.__sample_service.page(keyword, page_num, page_size, response)

        @router.get(path="/crawler-api/sample/crawler/json",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】爬虫 JSON',
                    description='【AppSampleRouter】爬虫 JSON',
                    response_model=AssertResponse,
                    status_code=200)
        async def sample_crawler_json(
                page_num: int = Query(0, description="page_num"),
                page_size: int = Query(10, description="page_size"),
                response: Response = None):
            return self.__sample_service.crawler_json(page_num, page_size, response)

        @router.get(path="/crawler-api/sample/crawler/html",
                    tags=['CRAWLER-APIS : 【AppSampleRouter】'],
                    summary='【AppSampleRouter】爬虫 HTML',
                    description='【AppSampleRouter】爬虫 HTML',
                    response_model=AssertResponse,
                    status_code=200)
        async def sample_crawler_html(
                id: str = Query('2203160954104521', description="id"),
                response: Response = None):
            return self.__sample_service.crawler_html(id, response)

    def config(self):
        return self.__router
