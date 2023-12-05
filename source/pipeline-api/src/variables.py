#!/usr/bin/python3
# file name: variables.py
# author: codepasser
# date: 2022/9/6

import os

APP_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

SOURCE_PATH = os.path.dirname(__file__)

ROOT_PATH = os.path.dirname(SOURCE_PATH)

INSTALL_PATH = os.path.dirname(ROOT_PATH)

# 项目路径
# Resource路径
CONFIG_PATH = os.path.join(ROOT_PATH, 'config')
# Banner 路径
BANNER_TXT_PATH = os.path.join(CONFIG_PATH, 'banner.txt')

# 应用级-配置文件
CONFIG_APP_INI_PATH = os.path.join(CONFIG_PATH, 'app.ini')
CONFIG_LOG_INI_PATH = os.path.join(CONFIG_PATH, 'log.ini')
CONFIG_LOG_JSON_PATH = os.path.join(CONFIG_PATH, 'uvicorn_log.json')

# 业务级-配置文件
CONFIG_APP_YAML_PATH = os.path.join(CONFIG_PATH, 'app.yaml')

# MyBatis Mapper
MAPPER_PATH = os.path.join(ROOT_PATH, 'mapper')
