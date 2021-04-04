from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("C:/data/.env")
sptfy_client_id = os.getenv("SPTFY_ID")
sptfy_client_secret = os.getenv("SPTFY_SECRET")

date = input("Which year do you want to retrieve music from? \nEnter date in the format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=sptfy_client_id,
        client_secret=sptfy_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]