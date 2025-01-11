def spotify_main():
    import os
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    env_client_id = os.getenv("CLIENT_ID")
    env_client_secret = os.getenv("CLIENT_SECRET")
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=env_client_id, client_secret=env_client_secret))

    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])


if __name__ == '__main__':
    spotify_main()