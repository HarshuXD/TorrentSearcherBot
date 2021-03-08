import os
from dotenv import load_dotenv
import logging

load_dotenv('config.env')

LOGGER = logging.getLogger(__name__)

def getConfig(name: str):
    return os.environ[name]
try:
    TOKEN = getConfig('BOT_TOKEN')
    API_HASH = getConfig('API_HASH')
    API_ID = int(getConfig('API_ID'))
except KeyError as e:
    LOGGER.error("One or more env variables missing! Exiting now")
    exit(1)

START_MESSAGE = getConfig("START_MESSAGE")
FOOTER_TEXT = getConfig("FOOTER_TEXT")
TORRENTS = {}