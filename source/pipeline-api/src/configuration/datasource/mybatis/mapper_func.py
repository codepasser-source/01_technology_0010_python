#!/usr/bin/python3
# file name: mapper_func.py
# author: codepasser
# date: 2022/9/21
from src.configuration import ConfigLogger
from src.configuration.datasource.mybatis.funs import like, time_format, default_fun_dict

CONSOLE_LOGGER = ConfigLogger.console_log()


# 函数容器
class PyFunction(object):

    def __init__(self):
        self.function_map = dict()

    def register_func(self, function_name: str, func):
        if function_name in self.function_map:
            CONSOLE_LOGGER.warning("function {} exist".format(function_name))
            return
        self.function_map[function_name] = func

    def get_func(self, function_name: str):
        if function_name in self.function_map:
            return self.function_map[function_name]
        return None

    def call_func(self, function_name: str, *args):
        func = self.get_func(function_name)
        if func and callable(func):
            return func(*args)


# 参数 转换函数
PY_PARAM_FUNCTION = PyFunction()
# 注册参数转换函数
for fun_name in default_fun_dict:
    PY_PARAM_FUNCTION.register_func(fun_name, default_fun_dict[fun_name])

# 返回值转换函数
PY_RESULT_FUNCTION = PyFunction()
