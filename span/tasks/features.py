from spotipy import Spotify
from span.models import Track, AudioFeatures
from typing import List
from loguru import logger


def chunk_list(items, chunk_size):
    chunks = []
    counter = 0
    working = []
    for item in items:
        if counter >= chunk_size:
            # split this chunk
            counter = 0
            chunks.append(working)
            working = []
        working.append(item)
        counter += 1

    # append final incomplete chunk
    chunks.append(working)

    return chunks


def process_segment(results) -> List[AudioFeatures]:
    features = []
    for item in results:
        model = AudioFeatures(
            acousticness=item["acousticness"],
            danceability=item["danceability"],
            energy=item["energy"],
            id=item["id"],
            instrumentalness=item["instrumentalness"],
            key=item["key"],
            liveness=item["liveness"],
            loudness=item["loudness"],
            mode=item["mode"],
            speechiness=item["speechiness"],
            tempo=item["tempo"],
            time_signature=item["time_signature"],
            valence=item["valence"],
        )
        features.append(model)
    return features


def get_audio_features(sp: Spotify, tracks: List[Track]) -> List[AudioFeatures]:
    track_ids = [track.id for track in tracks]
    # chunk the tracks
    chunks = chunk_list(track_ids, 100)
    features: List[AudioFeatures] = []

    # fetch data from api
    for chunk in chunks:
        results = sp.audio_features(chunk)
        features.extend(process_segment(results))

    logger.success(f"fetched {len(features)} audio features from spotify")

    # return the list
    return features
