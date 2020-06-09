from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True), verbose=False)

SPOTIFY_USER = getenv('SPOTIFY_USER')
SPOTIFY_SCOPE = 'user-library-read'