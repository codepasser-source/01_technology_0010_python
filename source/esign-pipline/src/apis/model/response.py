#!/usr/bin/python3
# file name: AssertResponse.py
# author: codepasser
# date: 2022/9/21
from pydantic import BaseModel


class AssertResponse(BaseModel):
    success: bool = True

    def __init__(self, success: bool = True):
        super().__init__()
        self.success = success
