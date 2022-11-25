#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

from src.configuration import Singleton, ConfigCrawlerYaml
from src.variables import CONFIG_CRAWLER_POF_YAML_PATH


@Singleton
class ConfigCrawlerPOFYaml(ConfigCrawlerYaml):
    # 定义构造方法
    def __init__(self):
        super().__init__(CONFIG_CRAWLER_POF_YAML_PATH)
