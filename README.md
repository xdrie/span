# spotify_analysis

spotify analysis

## dev

```
poetry install
```

## install
```
# from git
pip install git+https://git.rie.icu/xdrie/spotify_analysis.git
# or, from source
pip install .
```

## usage

configuration must be set in environment variables or in a `.env` file.

sample config:
```
SPOTIPY_CLIENT_ID="<redacted>"
SPOTIPY_CLIENT_SECRET="<redacted>"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SPOTIFY_USER="<username>"
```
