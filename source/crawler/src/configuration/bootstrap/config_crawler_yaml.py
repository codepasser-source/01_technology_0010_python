#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

from src.common.utils.file import File


class ConfigCrawlerYaml(object):
    __config = []

    # 定义构造方法
    def __init__(self, _config_path: str):
        self.__config = File(_config_path).get_yaml()

    def get(self):
        return self.__config[0]["CRAWLER"]

    def title(self):
        return self.__config[0]["CRAWLER"]['TITLE']

    def get_task(self, task: str = None):
        if task is None:
            return self.__config[0]["CRAWLER"]['TASKS']
        else:
            return self.__config[0]["CRAWLER"][task]
