#!/usr/bin/python3
# file name: async_caller.py
# author: codepasser
# date: 2022/11/14
from concurrent.futures import ThreadPoolExecutor
import threading
from threading import Thread


def AsyncCaller(async_fn):
    def wrapper(*args, **kwargs):
        thr = Thread(target=async_fn, args=args, kwargs=kwargs)
        thr.start()

        # with ThreadPoolExecutor(max_workers=2) as pool:
        #     # 向线程池提交一个task
        #     _future = pool.submit(async_fn)
        #
        #     # 定义获取结果的函数
        #     def get_result(_future):
        #         print(threading.current_thread().name + '运行结果：' + str(_future.result()))
        #     # _future.add_done_callback(get_result)

    return wrapper
