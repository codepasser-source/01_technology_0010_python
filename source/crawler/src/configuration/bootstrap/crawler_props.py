#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15
from src.configuration.bootstrap.crawler_args import CrawlerArgs


class PropsVar(CrawlerArgs):
    ID = 'id'
    PAGE = 'page'
    SIZE = 'size'
    TIMESTAMP = 'timestamp'


class PropsMethod(CrawlerArgs):
    GET = 'GET'
    POST = 'POST'


class PropsDataType(CrawlerArgs):
    JSON = 'JSON'
    HTML = 'HTML'


class PropsCharset(CrawlerArgs):
    UTF8 = 'utf-8'
    GBK = 'gbk'


class PropsConvertType(CrawlerArgs):
    TIMESTAMP = 'TIMESTAMP'
    DATE = 'DATE'
    SECOND = 'SECOND'
    MILLISECOND = 'MILLISECOND'
    MICROSECOND = 'MICROSECOND'
