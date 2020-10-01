# pylint:disable=R0903

"""
    Configuration File for Our Project
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Base Configuration
    """
    PROF_NAME = "base"
    DEBUG = False


class DevelopmentConfig(Config):
    """ Configuration for Development Environment
    """
    DEBUG = True
    PROF_NAME = "development"


class TestingConfig(Config):
    """ Configuration for Testing Environment
    """
    DEBUG = True
    PROF_NAME = "testing"


class ProductionConfig(Config):
    """ Configuration for Production Environment
    """
    DEBUG = False
    PROF_NAME = "production"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
