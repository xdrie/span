class Track:
    def __init__(self, artist, album, name, release_date, id, popularity, duration):
        self.artist: str = artist
        self.album: str = album
        self.name: str = name
        self.release_date = release_date
        self.id: str = id
        self.popularity: int = popularity
        self.duration: int = duration

    def __str__(self):
        return f"{self.name} ({self.duration // 1000}) [{self.release_date}] - {self.artist}, ({self.album})"

    @staticmethod
    def from_spotify(track):
        return Track(
            artist=track["artists"][0]["name"],
            album=track["album"]["name"],
            name=track["name"],
            release_date=track["album"]["release_date"],
            id=track["id"],
            popularity=track["popularity"],
            duration=track["duration_ms"],
        )


class LikedTrack(Track):
    def __init__(
        self, artist, album, name, release_date, id, popularity, duration, saved_at
    ):
        super().__init__(artist, album, name, release_date, id, popularity, duration)
        self.saved_at = saved_at

    def __str__(self):
        return f"{super.__str__()} (saved at {self.saved_at})"

    @staticmethod
    def copy_from(track: Track, saved_at):
        return LikedTrack(
            artist=track.artist,
            album=track.album,
            name=track.name,
            release_date=track.release_date,
            id=track.id,
            popularity=track.popularity,
            duration=track.duration,
            saved_at=saved_at,
        )


class AudioFeatures:
    def __init__(
        self,
        acousticness,
        danceability,
        energy,
        id,
        instrumentalness,
        key,
        liveness,
        loudness,
        mode,
        speechiness,
        tempo,
        time_signature,
        valence,
    ):
        self.acousticness: float = acousticness
        self.danceability: float = danceability
        self.energy: float = energy
        self.id: str = id
        self.instrumentalness: float = instrumentalness
        self.key: int = key
        self.liveness: float = liveness
        self.loudness: float = loudness
        self.mode: int = mode
        self.speechiness: float = speechiness
        self.tempo: float = tempo
        self.time_signature: int = time_signature
        self.valence: float = valence


class FeatureSet(Track, AudioFeatures):
    def __init__(
        self,
        # track
        artist,
        album,
        name,
        release_date,
        id,
        popularity,
        duration,
        # audio features
        acousticness,
        danceability,
        energy,
        instrumentalness,
        key,
        liveness,
        loudness,
        mode,
        speechiness,
        tempo,
        time_signature,
        valence,
    ):
        # initialize track
        Track.__init__(
            self, artist, album, name, release_date, id, popularity, duration
        )
        # initialize features
        AudioFeatures.__init__(
            self,
            acousticness,
            danceability,
            energy,
            id,
            instrumentalness,
            key,
            liveness,
            loudness,
            mode,
            speechiness,
            tempo,
            time_signature,
            valence,
        )
