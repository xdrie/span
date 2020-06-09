from loguru import logger
from spotipy import Spotify
import spotipy.util


def authenticate_client(user, scope) -> Spotify:
    # authenticate with spotify api
    token = spotipy.util.prompt_for_user_token(user, scope)
    if token:
        sp = spotipy.Spotify(auth=token)
        logger.success(f'authenticated to spotify as {user}')
        return sp
    else:
        logger.error(f"failed to get {scope} token for {user}")
