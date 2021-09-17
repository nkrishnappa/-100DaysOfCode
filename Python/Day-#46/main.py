import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"
# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()


# # date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date="2000-08-12"

# # <div class="chart-element__information__song font--semi-bold color--primary text--truncate">Incomplete</div>
# # <span class="chart-element__information__song text--truncate color--primary">Incomplete</span>
# # <span class="chart-element__information__song text--truncate color--primary">Bent</span>

# billboardURL = "http://www.billboard.com/charts/hot-100/" + date
# response = requests.get(url=billboardURL)
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup.prettify())


# all_song_text = soup.find_all(name="span", class_="chart-element__information__song")
# top_100_songs = [ song.getText() for song in all_song_text ]
# print(top_100_songs)