"""
This module tests the Configurations
"""
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfig(TestCase):
    """This class is used for Testing Dev Config

    Args:
        TestCase (Class): Original Test Case Class
    """

    def create_app(self):
        """Creates the app with Dev Config

        Returns:
            Flask App: Flask App with Dev Config
        """
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        """Tests that Dev App is successfully built with Debugging
        """
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    """This class is used for Testing Test Config

    Args:
        TestCase (Class): Original Test Case Class
    """

    def create_app(self):
        """Creates the app with Test Config

        Returns:
            Flask App: Flask App with Test Config
        """
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        """Tests that the Testing App is successfully built with Debugging
        """
        self.assertTrue(app.config['DEBUG'])


class TestProductionConfig(TestCase):
    """This class is used for Testing Prod Config

    Args:
        TestCase (Class): Original Test Case Class
    """

    def create_app(self):
        """Creates the app with Prod Config

        Returns:
            Flask App: Flask App with Prod Config
        """
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        """Tests that the Prod App is successfully built with Debugging
        """
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
