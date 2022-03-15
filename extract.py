import spotipy
import os
import sys

from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

#Client Authorization Code Flow - Working with the spotify API with user authentication.
def auth_code_flow():
    """
    Demonstrates how to extract a Spotify user's 50 most recent saved tracks 
    and save the extracted data to a '.txt' file. Authentication is handled
    using the Spotipy package's Authorization Code Flow method
    """
    scope = "user-library-read"
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = 'https://localhost:8080/callback'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope))

    results = sp.current_user_saved_tracks(limit=50)

    for _, item in enumerate(results['items']):
        track = item['track']
        res = "Title:",track['name'],"\nBy:",track['artists'][0]['name'],"\n------------------------------------\n"
        new_res = ''.join(res)
        #Save extracted data to a TXT file
        try:
            with open('my_fave_music.txt', 'a') as f:
                f.write(new_res)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")


#Client Credentials Flow - Working with the spotify API without user authentication.
def credentials_flow():
    """
    Demonstrates how to extract all tracks from the Spotify top 50 (Nigerian Version) playlist  
    and save the extracted data to a '.txt' file. Authentication is handled
    using the Spotipy package's Client Credentials Flow method
    """
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv('Client_ID'),
        client_secret=os.getenv('Client_SECRET')
        )
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLw80jjcctV1?si=51bfe711408642da"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

    for track in sp.playlist_tracks(playlist_URI)["items"]:
        # Track URI
        track_uri = track["track"]["uri"]
        
        #Track name
        track_name = track["track"]["name"]
        
        #Artist Details
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        
        #Artist Name
        artist_name = track["track"]["artists"][0]["name"]

        res = "Title:",track_name,"\nBy:",artist_name,"\n------------------------------------\n"
        new_res = ''.join(res)
        #Save extracted data to a TXT file
        try:
            with open('top_50_Nigeria.txt', 'a') as f:
                f.write(new_res)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

# Calling Authentication Flow function
auth_code_flow()

# Calling Credentials Flow Function
credentials_flow()
