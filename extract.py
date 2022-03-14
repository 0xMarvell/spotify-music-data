import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('Client_ID'), client_secret=os.getenv('Client_SECRET'))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

