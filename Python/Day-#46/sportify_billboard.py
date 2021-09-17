from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date="2021-08-12"
billboardURL = "http://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboardURL)
soup = BeautifulSoup(response.text, "html.parser")
all_song_text = soup.find_all(name="span", class_="chart-element__information__song")
top_100_songs = [ song.getText() for song in all_song_text ]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# print(user_id) # 31lpng3ftzlxdcoug2r7wrcxks6q
# song = "I Will Love Again"
# year = "2000"
# result = sp.search(q=f"track:{song} year:{year}", type="track")
# print(result["tracks"]["items"][0]["uri"]) 
# # spotify:track:1raT3L0NJtc10t7xNgHJZ1

year = int(date.split("-")[0])
list_of_spotify_songs = []
for song_title in top_100_songs:
    result = sp.search(q=f"track:{song_title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        list_of_spotify_songs.append(uri)
    except IndexError:
        print(f"Not able to find the song -  {song_title}")

# print(list_of_spotify_songs)


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=list_of_spotify_songs)
