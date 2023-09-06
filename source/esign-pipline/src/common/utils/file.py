#!/usr/bin/python3
# file name: file.py
# author: codepasser
# date: 2022/9/6

# !/usr/bin/python3
# file name: file
# author: codepasser
# date: 2019/12/11
import csv
import yaml


class File:
    path = None

    def __init__(self, path):
        self.path = path

    def output(self):
        with open(self.path, 'r') as f:  # 打开文件
            data = f.read()  # 读取文件
        print(data)
        f.close()

    def get_yaml(self):
        _yaml_config: list = []
        with open(self.path, 'rb') as f:
            # yaml文件通过---分节，多个节组合成一个列表
            data = yaml.safe_load_all(f)
            # safe_load_all方法得到的是一个迭代器，需要使用list()方法转换为列表
            _yaml_config = list(data)
            f.close()
        return _yaml_config

    def export_csv(self, filename, headers, rows):
        with open(self.path + '/' + filename, mode='a', encoding='utf-8-sig', newline='') as csv_file:
            outDictWriter = csv.DictWriter(csv_file, headers)
            outDictWriter.writeheader()
            writer = csv.writer(csv_file)
            writer.writerows(rows)
