import sys
from loguru import logger
import settings
from auth import authenticate_client
from spotipy import Spotify
import click
import jsonpickle
import models

# ensure args
if not settings.SPOTIFY_USER:
    logger.error("SPOTIFY_USER not set.")
    sys.exit(1)


def get_client() -> Spotify:  # get an authenticated client
    return authenticate_client(settings.SPOTIFY_USER, settings.SPOTIFY_SCOPE)


@click.group()
@click.option("-v", "--verbose", is_flag=True)
def cli(verbose):
    """SPAN (SPotify-ANalyzer) liberates data from Spotify for local analysis"""
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="TRACE")
        logger.trace("verbose mode enabled")


@cli.group()
def fetch():
    """Fetch remote lists via the Spotify API"""
    pass


@fetch.command()
def liked():
    """Get liked songs (saved tracks in spotify library)"""
    sp = get_client()

    from tasks.library import get_liked_tracks

    liked_tracks = get_liked_tracks(sp)

    # export data
    sys.stdout.write(jsonpickle.encode(liked_tracks))


@cli.group()
def analyze():
    """Analyze data using the Spotify API"""
    pass


@analyze.command()
def features():
    """Analyze track features (read from stdin)"""
    sp = get_client()

    raw_data = sys.stdin.read()
    tracks = jsonpickle.decode(raw_data)

    # get track features
    from tasks.features import get_audio_features

    features = get_audio_features(sp, tracks)
    
    # export data
    sys.stdout.write(jsonpickle.encode(features))


cli()
