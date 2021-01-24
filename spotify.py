from os import environ
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from typing import List, Dict

# Authenticate to Spotify
def authenticate(cliend_id: str, client_secret: str) -> spotipy.client.Spotify:
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=cliend_id,
            client_secret=client_secret
        )
    )
    return sp

# Number of tracks available in the playlist
def get_pl_length(sp: spotipy.client.Spotify, pl_uri: str) -> int:
    return sp.playlist_tracks(
        pl_uri,
        offset=0,
        fields="total"
    )["total"]

# Get all the artist info about each track of the playlist.
def get_tracks_artist_info(sp: spotipy.client.Spotify, pl_uri: str) -> List[List[Dict]]:
    artists_info = list()
    # Start retrieving tracks from the beginning of the playlist
    offset = 0
    pl_length = get_pl_length(sp, pl_uri)

    # Playlist track retrieval only fetches 100 tracks at a time, hence\
    # the loop to keep retrieving until we reach the end of the playlist
    while offset != pl_length:
        # Get the next batch of tracks
        pl_tracks = sp.playlist_tracks(
            pl_uri,
            offset=offset,
            fields="items.track"
        )

        # Get the list with the info about the artists of each track from the\
        # latest batch and append it to the running list
        [artists_info.append(pl_item["track"]["artists"])
            for pl_item in pl_tracks["items"]]

        # Update the offset
        offset += len(pl_tracks["items"])

    return artists_info


# Calculate the frequency of each artist in the playlist
def get_artist_counts(artists_info: List[List[Dict]]) -> Dict[str, int]:
    artist_counts = dict()

    # Loop through the lists of artist information
    for track_artists in artists_info:
        # Loop through the artists associated with the current track
        for artist in track_artists:
            # Update the current artist's frequency
            artist_name = artist["name"]
            if artist_name in artist_counts:
                artist_counts[artist_name] += 1
            else:
                artist_counts[artist_name] = 1

    return artist_counts

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(str(i)+": "+track['artists'][0]['name'] + " - " + track['name'])
 	
if __name__ == "__main__":
    # Get the credentials from environment variables
    CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")
    # Get a Spotify authenticated instance
    sp_instance = authenticate(CLIENT_ID, CLIENT_SECRET)
    #print(sp_instance)

    username = "everaldo.pessoa"
    playlists = sp_instance.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print()
            print(playlist['name'] + "("+playlist['id']+")")	
            print('total tracks:', playlist['tracks']['total'])
            results = sp_instance.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp_instance.next(tracks)
                show_tracks(tracks)
				
			# Get the artist information for all tracks of the playlist            			
            #artists_info = get_tracks_artist_info(sp_instance, playlist['id'])
            #print(artists_info)
			
            # Get the frequencies of each artist
            #artists_counts = get_artist_counts(artists_info)
            #print(artists_counts)
            #print()
			
    
