#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

import os
from src.configuration.bootstrap.crawler_args import CrawlerArgs


class Env(CrawlerArgs):
    PROFILE = 'CRAWLER_PROFILE'


class Profile(CrawlerArgs):
    DEV = 'dev'
    UAT = 'uat'
    SIM = 'sim'
    PROD = 'prod'

    @staticmethod
    def get():
        _env = os.environ
        return _env.get(Env.PROFILE.key, Profile.DEV.value)
