#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

import os
from src.configuration.bootstrap.define_args import DefineArgs


class Env(DefineArgs):
    PROFILE = 'PROFILE'


class Profile(DefineArgs):
    DEV = 'dev'
    UAT = 'uat'
    SIM = 'sim'
    PROD = 'prod'

    @staticmethod
    def get():
        _env = os.environ
        return _env.get(Env.PROFILE.key, Profile.DEV.value)
