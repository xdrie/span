class Track:
    def __init__(self, artist, album, name, release_date, id, popularity, duration):
        self.artist = artist
        self.album = album
        self.name = name
        self.release_date = release_date
        self.id = id
        self.popularity = popularity
        self.duration = duration

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

class LikedTrack:
    def __init__(self, track, saved_at):
        self.track = track
        self.saved_at = saved_at
    
    def __str__(self):
        return f"{str(self.track)} (saved at {self.saved_at})"