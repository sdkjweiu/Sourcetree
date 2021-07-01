import sys
sys.path.append('d:/Sourcetree_account')
import email_adr
import pymysql_con


class Config:
    SECRET_KEY = 'hard to guess string'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>' #example.com 은 자동으로 메일값이 바뀜

    @staticmethod
    def init_app(app):
        pass



class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True

    
    MAIL_USERNAME = email_adr.MAIL_USERNAME
    MAIL_PASSWORD = email_adr.MAIL_PASSWORD
    
    DB_USER = pymysql_con.user
    DB_PASSWD = pymysql_con.passwd


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}