#!/usr/bin/python3
# file name: config_app_ini.py
# author: codepasser
# date: 2022/9/6
import os.path
import configparser

from src.configuration import Singleton
from src.configuration.bootstrap.environments import Profile, Env
from src.variables import CONFIG_PATH, CONFIG_APP_INI_PATH


@Singleton
class ConfigAppIni:
    __config = {}

    # 定义构造方法
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(self.load_profile_config())

    @staticmethod
    def load_profile_config():
        _config_path = CONFIG_APP_INI_PATH
        if Profile.get() is not None:
            _profile_config = 'app-{}.ini'.format(Profile.get())
            _config_path = os.path.join(CONFIG_PATH, _profile_config)
            if os.path.exists(_config_path) is False:
                _config_path = CONFIG_APP_INI_PATH
        print(_config_path)
        return _config_path

    def get(self, section, option):
        return self.__config.get(section=section, option=option)
