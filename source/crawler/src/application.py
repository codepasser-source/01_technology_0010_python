#!/usr/bin/python3
# file name: app.py
# author: codepasser
# date: 2022/9/9

import os
import sys
import uvicorn

# 头部引入项目目录
APP_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
MAIN_PATH = os.path.abspath(__file__)
sys.path.append(APP_PATH)

from fastapi import FastAPI
from src.configuration import ConfigAppIni
from src.common import File

from src.router import AppRouter, AppDebugRouter, AppSampleRouter, AppCrawlerRouter

from src.variables import BANNER_TXT_PATH, CONFIG_LOG_JSON_PATH

api = FastAPI(
    title='Swagger API 文档',
    description='CODEPASSER PLATFORM API v1.0',
    version='1.0.0.RELEASE',
    docs_url='/docs',
    redoc_url='/redoc'
)

# Application Router
api.include_router(router=AppRouter().config())

# Application Debug Router
api.include_router(router=AppDebugRouter().config())

# Application Sample Router
api.include_router(router=AppSampleRouter().config())

# Application Crawler Router
api.include_router(router=AppCrawlerRouter().config())

if __name__ == '__main__':
    host = ConfigAppIni().get('server', 'host')
    port = int((ConfigAppIni().get('server', 'port')))
    context = ConfigAppIni().get('server', 'context')

    File(BANNER_TXT_PATH).output()

    # uvicorn app:api --reload
    uvicorn.run(app='application:api', host=host, port=port, log_config=CONFIG_LOG_JSON_PATH)
