from os import getenv
from dotenv import load_dotenv
load_dotenv(verbose=True)

SPOTIFY_USER = getenv('SPOTIFY_USER')
SPOTIFY_SCOPE = 'user-library-read'