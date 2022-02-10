import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv("/Users/Ryuuuu/PycharmProjects/Spotify_Playlist/.env")


Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")

# Scraping Billboard 100
date = input("Let's make a playlist of those days! Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name = "h3", id = "title-of-a-story")

song_names = [song.getText() for song in song_names_spans][6:403][::4]  #extract only song names
song_names = [song_name.replace("\n","") for song_name in song_names]   #remove "\n"

print(song_names)

# #Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= Client_ID,
        client_secret= Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
)
)

user_id = sp.current_user()["id"]
# print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




#https://open.spotify.com/collection/playlists