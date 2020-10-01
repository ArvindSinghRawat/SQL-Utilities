# pylint:disable=R0903

"""
    Configuration File for Our Project
"""
import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Base Configuration
    """
    PROF_NAME = "base"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')


class DevelopmentConfig(Config):
    """ Configuration for Development Environment
    """
    DEBUG = True
    PROF_NAME = "development"
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DB_URL']


class TestingConfig(Config):
    """ Configuration for Testing Environment
    """
    TESTING = True
    DEBUG = True
    PROF_NAME = "testing"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DB_URL']


class ProductionConfig(Config):
    """ Configuration for Production Environment
    """
    DEBUG = False
    PROF_NAME = "production"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ['PROD_DB_URL']


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
