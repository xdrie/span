from span.models import Track, AudioFeatures, FeatureSet
from typing import List
from loguru import logger
import pandas as pd

def to_csv(raw_data: str) -> str:
    df = pd.read_json(raw_data)
    csv_data = df.to_csv(index=True)
    return csv_data

def make_feature_sets(tracks: List[Track], features: List[AudioFeatures]) -> List[FeatureSet]:
    logger.info(f"merging {len(tracks)} track data with {len(features)} feature data")

    feature_sets: List[FeatureSet] = []
    
    # go through all the feature data
    for song_features in features:
        # find a track with matching id
        track = next(track for track in tracks if track.id == song_features.id)
        feature_set = FeatureSet(
            # track
            track.artist,
            track.album,
            track.name,
            track.release_date,
            track.id,
            track.popularity,
            track.duration,
            # features
            song_features.acousticness,
            song_features.danceability,
            song_features.energy,
            song_features.instrumentalness,
            song_features.key,
            song_features.liveness,
            song_features.loudness,
            song_features.mode,
            song_features.speechiness,
            song_features.tempo,
            song_features.time_signature,
            song_features.valence,
        )
        feature_sets.append(feature_set)

    logger.success(f"crunched into {len(feature_sets)} feature sets")

    return feature_sets
