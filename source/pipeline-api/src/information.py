#!/usr/bin/python3
# file name: information.py
# author: codepasser
# date: 2022/9/6

import time, ntplib

from src.configuration import ConfigAppIni, ConfigLogger
from src.configuration.bootstrap.environments import Profile
from src.variables import *

UVICORN_LOGGER = ConfigLogger.uvicorn_log()


class ApplicationInfo:

    @staticmethod
    def info():
        UVICORN_LOGGER.info('<********* environment *******>')
        UVICORN_LOGGER.info('APP_PATH                  : %s ' % APP_PATH)
        UVICORN_LOGGER.info('SOURCE_PATH               : %s ' % SOURCE_PATH)
        UVICORN_LOGGER.info('ROOT_PATH                 : %s ' % ROOT_PATH)
        UVICORN_LOGGER.info('INSTALL_PATH              : %s ' % INSTALL_PATH)

        UVICORN_LOGGER.info('CONFIG_PATH               : %s ' % CONFIG_PATH)
        UVICORN_LOGGER.info('BANNER_TXT_PATH           : %s ' % BANNER_TXT_PATH)
        UVICORN_LOGGER.info('CONFIG_LOG_INI_PATH       : %s ' % CONFIG_LOG_INI_PATH)
        UVICORN_LOGGER.info('CONFIG_APP_INI_PATH       : %s ' % CONFIG_APP_INI_PATH)
        UVICORN_LOGGER.info('<********* environment *******/>')

        UVICORN_LOGGER.info('<********* application *******>')

        UVICORN_LOGGER.info('Environment profile       : %s' % Profile.get())
        UVICORN_LOGGER.info('Environment profile config: %s' % ConfigAppIni().load_profile_config())
        UVICORN_LOGGER.info('[server][host]            : %s' % ConfigAppIni().get('server', 'host'))
        UVICORN_LOGGER.info('[server][port]            : %s' % ConfigAppIni().get('server', 'port'))
        UVICORN_LOGGER.info('[server][context]         : %s' % ConfigAppIni().get('server', 'context'))

        UVICORN_LOGGER.info('[app][storage]            : %s' % ConfigAppIni().get('app', 'storage'))
        UVICORN_LOGGER.info('[app][user-agent]         : %s' % ConfigAppIni().get('app', 'user-agent'))

        UVICORN_LOGGER.info('[datasource][host]        : %s' % ConfigAppIni().get('datasource', 'host'))
        UVICORN_LOGGER.info('[datasource][port]        : %s' % ConfigAppIni().get('datasource', 'port'))
        UVICORN_LOGGER.info('[datasource][user]        : %s' % ConfigAppIni().get('datasource', 'user'))
        UVICORN_LOGGER.info('[datasource][database]    : %s' % ConfigAppIni().get('datasource', 'database'))

        c = ntplib.NTPClient()
        ntp_server = ConfigAppIni().get('ntp', 'server')
        response = c.request(ntp_server, version=3)
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        _time = time.strftime('%X', time.localtime(ts))

        UVICORN_LOGGER.info('[ntp][host]               : %s ' % ntp_server)
        UVICORN_LOGGER.info('[ntp][timestamp]          : %s ' % ts)
        UVICORN_LOGGER.info('[ntp][date]               : %s ' % _date)
        UVICORN_LOGGER.info('[ntp][time]               : %s ' % _time)

        UVICORN_LOGGER.info('[poi][limit]              : %s' % ConfigAppIni().get('poi', 'limit'))

        UVICORN_LOGGER.info('[scheduler][threads]      : %s' % ConfigAppIni().get('scheduler', 'threads'))
        UVICORN_LOGGER.info('[scheduler][interval]     : %s' % ConfigAppIni().get('scheduler', 'interval'))
        UVICORN_LOGGER.info('<********* application ********/>')
