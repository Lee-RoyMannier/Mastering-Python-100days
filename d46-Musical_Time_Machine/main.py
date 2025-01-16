from bs4 import BeautifulSoup
import requests
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv(".env")

music_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
try:
    date_formating = datetime.strptime(music_date, "%Y-%m-%d")
except ValueError:
    print("Please enter a valid date in this format: YYYY-MM-DD")
else:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    url = f"https://www.billboard.com/charts/hot-100/{music_date}"
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names_spans = soup.select("li ul li h3")
    titles = [title.getText().split() for title in song_names_spans]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Lee Roy"
    ))
    song_urls = []
    user_id = sp.current_user()["id"]
    year = music_date.split("-")[0]
    playlist = sp.user_playlist_create(user_id, name=f"Billboard 100 {music_date}", public=False)
    for song in titles:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            track = result["tracks"]["items"][0]["uri"]
            song_urls.append(track)
        except IndexError:
            print("No track found for ",song)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)

