import os

# Env Configs
APP_ENV = os.getenv("APP_ENV")
APP_DEBUG = os.getenv("APP_DEBUG").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
ALLOWED_CORS_ORIGINS = os.getenv("ALLOWED_CORS_ORIGINS").split(',')

# Mongo
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
TEST_MONGO_DATABASE = os.getenv("TEST_MONGO_DATABASE")
