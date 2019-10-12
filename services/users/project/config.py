#!/usr/bin/env python3
import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG_TB_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(BaseConfig):
    """Production configuration"""

    passSQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
