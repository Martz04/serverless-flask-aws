import os

IS_OFFLINE = True if str(os.environ.get("IS_OFFLINE")).lower() == "true" else False

if IS_OFFLINE:
    PORT = int(os.environ.get('APP_BIND_PORT'))
    HOST = os.environ.get('APP_BIND_HOST')

    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = int(os.environ.get("DB_PORT"))

REGION_NAME = os.environ.get("REGION_NAME")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")
