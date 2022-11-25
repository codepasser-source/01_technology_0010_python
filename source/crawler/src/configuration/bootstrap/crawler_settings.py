#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

from src.configuration.bootstrap.crawler_args import CrawlerArgs


class CrawlerSettings(CrawlerArgs):
    TITLE = 'TITLE'
    URL = 'URL'
    METHOD = 'METHOD'
    DATA_TYPE = 'DATA-TYPE'
    PAGINATION = 'PAGINATION'
    PAGINATION_PAGE = 'PAGINATION-PAGE'
    PAGINATION_SIZE = 'PAGINATION-SIZE'
    PARAMS = 'PARAMS'
    PAYLOAD = 'PAYLOAD'
    DATA_MAPPER = 'DATA-MAPPER'
    DATA_TOTAL_MAPPER = 'DATA-TOTAL-MAPPER'
    DATA_CONVERT = 'DATA-CONVERT'
    DB_TABLE = 'DB-TABLE'
    DB_MAPPING = 'DB-MAPPING'
