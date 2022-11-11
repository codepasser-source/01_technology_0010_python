#!/usr/bin/python3
# file name: information.py
# author: codepasser
# date: 2022/9/6

import time, ntplib

from src.configuration import ConfigAppIni, ConfigLogger
from src.variables import *

CONSOLE_LOGGER = ConfigLogger.console_log()


class ApplicationInfo:

    @staticmethod
    def info():
        CONSOLE_LOGGER.debug('<********* environment *******>')
        CONSOLE_LOGGER.debug('APP_PATH                  : %s ' % APP_PATH)
        CONSOLE_LOGGER.debug('SOURCE_PATH               : %s ' % SOURCE_PATH)
        CONSOLE_LOGGER.debug('ROOT_PATH                 : %s ' % ROOT_PATH)
        CONSOLE_LOGGER.debug('INSTALL_PATH              : %s ' % INSTALL_PATH)

        CONSOLE_LOGGER.debug('CONFIG_PATH               : %s ' % CONFIG_PATH)
        CONSOLE_LOGGER.debug('BANNER_TXT_PATH           : %s ' % BANNER_TXT_PATH)
        CONSOLE_LOGGER.debug('CONFIG_LOG_INI_PATH       : %s ' % CONFIG_LOG_INI_PATH)
        CONSOLE_LOGGER.debug('CONFIG_APP_INI_PATH       : %s ' % CONFIG_APP_INI_PATH)
        CONSOLE_LOGGER.debug('<********* environment *******/>')

        CONSOLE_LOGGER.debug('<********* application *******>')

        CONSOLE_LOGGER.debug('[server][host]            : %s' % ConfigAppIni().get('server', 'host'))
        CONSOLE_LOGGER.debug('[server][port]            : %s' % ConfigAppIni().get('server', 'port'))
        CONSOLE_LOGGER.debug('[server][context]         : %s' % ConfigAppIni().get('server', 'context'))

        CONSOLE_LOGGER.debug('[app][storage]            : %s' % ConfigAppIni().get('app', 'storage'))
        CONSOLE_LOGGER.debug('[app][user-agent]         : %s' % ConfigAppIni().get('app', 'user-agent'))

        CONSOLE_LOGGER.debug('[datasource][host]        : %s' % ConfigAppIni().get('datasource', 'host'))
        CONSOLE_LOGGER.debug('[datasource][port]        : %s' % ConfigAppIni().get('datasource', 'port'))
        CONSOLE_LOGGER.debug('[datasource][user]        : %s' % ConfigAppIni().get('datasource', 'user'))
        CONSOLE_LOGGER.debug('[datasource][database]    : %s' % ConfigAppIni().get('datasource', 'database'))

        c = ntplib.NTPClient()
        ntp_server = ConfigAppIni().get('ntp', 'server')
        response = c.request(ntp_server, version=3)
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        _time = time.strftime('%X', time.localtime(ts))

        CONSOLE_LOGGER.debug('[ntp][host]               : %s ' % ntp_server)
        CONSOLE_LOGGER.debug('[ntp][timestamp]          : %s ' % ts)
        CONSOLE_LOGGER.debug('[ntp][date]               : %s ' % _date)
        CONSOLE_LOGGER.debug('[ntp][time]               : %s ' % _time)

        CONSOLE_LOGGER.debug('[poi][limit]              : %s' % ConfigAppIni().get('poi', 'limit'))

        CONSOLE_LOGGER.debug('[scheduler][threads]      : %s' % ConfigAppIni().get('scheduler', 'threads'))
        CONSOLE_LOGGER.debug('[scheduler][interval]     : %s' % ConfigAppIni().get('scheduler', 'interval'))
        CONSOLE_LOGGER.debug('<********* application ********/>')
