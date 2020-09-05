import sys
from loguru import logger
from spotipy import Spotify
import typer
import jsonpickle
from span import settings
from span import models
from span.auth import authenticate_client


def get_client() -> Spotify:  # get an authenticated client
    if not settings.SPOTIFY_USER:  # ensure args
        logger.error("SPOTIFY_USER not set.")
        raise typer.Exit(1)
    return authenticate_client(settings.SPOTIFY_USER, settings.SPOTIFY_SCOPE)


app = typer.Typer()

fetch_app = typer.Typer()
app.add_typer(fetch_app, name="fetch", help="Fetch remote lists via the Spotify API")

crunch_app = typer.Typer()
app.add_typer(crunch_app, name="crunch", help="Crunch downloaded data")

analyze_app = typer.Typer()
app.add_typer(analyze_app, name="analyze", help="Analyze data")


@fetch_app.command("liked")
def fetch_liked():
    """Get liked songs (saved tracks in spotify library)"""
    sp = get_client()

    from span.tasks.library import get_liked_tracks

    liked_tracks = get_liked_tracks(sp)

    # export data
    sys.stdout.write(jsonpickle.encode(liked_tracks))


@fetch_app.command("features")
def fetch_features():
    """Fetch track features (given list of tracks)"""
    sp = get_client()

    raw_data = sys.stdin.read()
    tracks = jsonpickle.decode(raw_data)

    # get track features
    from span.tasks.features import get_audio_features

    features = get_audio_features(sp, tracks)

    # export data
    sys.stdout.write(jsonpickle.encode(features))

@crunch_app.command("to_csv")
def crunch_to_csv(source_data: typer.FileText):
    """Crunch a list of data classes to CSV"""

    from span.tasks.crunch import to_csv

    csv_data = to_csv(source_data.read())

    # export data
    sys.stdout.write(csv_data)

@crunch_app.command("feature_sets")
def crunch_feature_sets(track_list: typer.FileText, feature_data: typer.FileText):
    """Combine track list and feature data into a list of Feature Sets"""

    tracks = jsonpickle.decode(track_list.read())
    features = jsonpickle.decode(feature_data.read())

    from span.tasks.crunch import make_feature_sets

    feature_sets = make_feature_sets(tracks, features)

    # export data
    sys.stdout.write(jsonpickle.encode(feature_sets))


@app.callback()
def cli_main(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """SPAN (SPotify-ANalyzer) liberates data from Spotify for local analysis"""
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="TRACE")
        logger.trace("verbose mode enabled")


def main():
    app()
