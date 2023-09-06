#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

from enum import Enum
from types import DynamicClassAttribute


class DefineArgs(Enum):

    @DynamicClassAttribute
    def key(self):
        return self._value_
