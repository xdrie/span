# spotify_analysis

spotify analysis

## dev

```sh
poetry install
```

## install
```sh
# from git
pip install git+https://git.rie.icu/xdrie/spotify_analysis.git
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
