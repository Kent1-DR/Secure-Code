from flask import Flask


class Config(object):
    TESTING = True
    DEBUG = False
    FLASK_RUN_PORT=80
    DB_SERVER = '0.0.0.0'


class Basicconf(Config):
    TESTING = True
    DEBUG = False
    FLASK_RUN_PORT=80
    DB_SERVER = '0.0.0.0'