# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ 系统参数配置 """
    ## 数据库
    DB_CONFIG = {
        'SERVER':r'DESKTOP-16D8IE2\SQLEXPRESS',
        'DATABASE':'test',
        'UID':'sa',
        'PWD':'Chinkun65613303'
    }

    ## Flask Mail
    MAIL_CONFIG = {
        'MAIL_SERVER':'smtp.mxhichina.com',
        'MAIL_PORT': 25,
        'MAIL_USE_TLS': False,
        'MAIL_USE_SSL' :False,
        'MAIL_DEBUG': False,
        'MAIL_USERNAME': 'kxqiu@chinkun.cn',
        'MAIL_PASSWORD' : 'Xx19910814',
        'DEFAULT_MAIL_SENDER' : None
    }

