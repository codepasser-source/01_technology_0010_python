#!/usr/bin/python3
# file name: config_app_yaml.py
# author: codepasser
# date: 2022/9/6
from src.configuration import Singleton
from src.variables import CONFIG_APP_YAML_PATH
from src.common import File


@Singleton
class ConfigAppYaml:
    __config = []

    # 定义构造方法
    def __init__(self):
        self.__config = File(CONFIG_APP_YAML_PATH).get_yaml()

    def get(self):
        return self.__config[0]['app']

    def get_requ_error(self):
        return self.__config[0]['app']['http-status']['requ-error']

    def get_resp_error(self):
        return self.__config[0]['app']['http-status']['resp-error']

    def sample_json_api(self):
        return self.__config[0]["app"]["sample-json-api"]

    def sample_html_api(self):
        return self.__config[0]["app"]["sample-html-api"]
