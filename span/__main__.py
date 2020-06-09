from sys import exit
from loguru import logger
import settings
from auth import authenticate_client

# ensure args
if not settings.SPOTIFY_USER:
    logger.error('SPOTIFY_USER not set.')
    exit(1)

# get an authenticated client
sp = authenticate_client(settings.SPOTIFY_USER, settings.SPOTIFY_SCOPE)
