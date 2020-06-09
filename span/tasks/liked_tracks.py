from spotipy import Spotify
from models import Track, LikedTrack
from typing import List
from loguru import logger


def process_segment(results) -> List[LikedTrack]:
    tracks = []
    for item in results["items"]:
        track_obj = item["track"]
        track_add_date = item["added_at"]

        # get track meta
        track_model = Track.from_spotify(track_obj)
        liked_track = LikedTrack(track=track_model, saved_at=track_add_date)
        tracks.append(liked_track)
    return tracks


def get_liked_tracks(sp: Spotify) -> List[LikedTrack]:
    # get saved tracks
    results = sp.current_user_saved_tracks()
    liked_tracks: List[LikedTrack] = []
    liked_tracks.extend(process_segment(results))
    while results["next"]:
        results = sp.next(results)
        liked_tracks.extend(process_segment(results))

    logger.trace('fetched user saved tracks from spotify')

    # return the list
    return liked_tracks
