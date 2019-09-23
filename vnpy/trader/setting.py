"""
Global setting of VN Trader.
"""

from logging import CRITICAL

from .utility import load_json

SETTINGS = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "mddata.api": "rqdata",

    "rqdata.username": "",
    "rqdata.password": "",

    "jqdata.username": "",
    "jqdata.password": "",

    "database.driver": "mysql",  # see database.Driver
    "database.database": "neuralnetwork",  # for sqlite, use this as filepath
    "database.host": "172.16.100.173",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "111111",
    "database.authentication_source": "admin",  # for mongodb
}

# Load global setting from json file.
SETTING_FILENAME = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))


def get_settings(prefix: str = ""):
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}
