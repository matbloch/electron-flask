import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'REPLACE ME')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
