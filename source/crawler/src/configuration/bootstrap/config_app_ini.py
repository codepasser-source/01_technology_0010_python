#!/usr/bin/python3
# file name: config_app_ini.py
# author: codepasser
# date: 2022/9/6

import configparser

from src.variables import CONFIG_APP_INI_PATH


class ConfigAppIni:
    __config = {}

    # 定义构造方法
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(CONFIG_APP_INI_PATH)

    def get(self, section, option):
        return self.__config.get(section=section, option=option)
