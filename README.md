
# span

span (SPotify ANalyzer) is a CLI for managing exported Spotify data.

## features

+ fetch
  + [liked tracks](https://developer.spotify.com/documentation/web-api/reference/library/get-users-saved-tracks/)
  + [track features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)
+ crunch
  + combine track features and track list into "song feature sets"

## dev

```sh
poetry install
```

## install
```sh
# from git
pip install git+https://github.com/xdrie/span
# or, from source
pip install .
```

## usage

configuration must be set in environment variables or in a `.env` file.

the `SPOTIPY_*` variables should be set as described in the [Spotipy docs](https://spotipy.readthedocs.io/en/2.12.0/#authorization-code-flow)
to obtain an authorization token. the token will be cached in a file called `.cache-*` in the current directory.

a sample configuration:
```sh
SPOTIPY_CLIENT_ID="<redacted>"
SPOTIPY_CLIENT_SECRET="<redacted>"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SPOTIFY_USER="<username>"
```
