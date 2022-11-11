#!/usr/bin/python3
# file name: config_app_yaml.py
# author: codepasser
# date: 2022/9/6

from src.variables import CONFIG_APP_YAML_PATH
from src.common import File


class ConfigAppYaml:
    __config = []

    # 定义构造方法
    def __init__(self):
        self.__config = File(CONFIG_APP_YAML_PATH).get_yaml()

    def get(self):
        return self.__config[0]['app']

    def poi_api(self):
        return self.__config[0]['app']['poi-api']

    def poi(self):
        return self.__config[0]['app']['poi']
