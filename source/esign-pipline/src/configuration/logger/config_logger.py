#!/usr/bin/python3
# file name: config_logger.py
# author: codepasser
# date: 2022/9/6

import logging


# from logging.config import fileConfig
# from src.variables import CONFIG_LOG_INI_PATH
# fileConfig(CONFIG_LOG_INI_PATH)

class ConfigLogger:

    @staticmethod
    def console_log():
        return logging.getLogger('console')

    @staticmethod
    def system_log():
        return logging.getLogger('system')

    @staticmethod
    def uvicorn_log():
        return logging.getLogger('uvicorn')
