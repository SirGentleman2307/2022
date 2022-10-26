import json
from urllib import response
import requests

USER_ID = '21pew2rqfu6ajvpuj5qjh2a4a'

CREATE_PLAYLIST_URL = f'https://api.spotify.com/v1/{USER_ID}/playlists'
ACCESS_TOKEN = ''


def createPlaylist(name, public):
    response = requests.post(
        CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp


def main():
    playlist = createPlaylist(
        name = "Cool Code",
        public = False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()