import datetime
from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

playlistId="YOUR PLAY LIST HERE"
playlist = ytmusic.get_playlist(playlistId)
print("Playlist: "+playlist['title'])
print("Author: "+playlist['author']['name'])
print("Track Count: "+str(playlist['trackCount']))
print("Duration: "+str(playlist['duration']))
print("\n")

track_list=[]
with open('track_list.txt', encoding='iso-8859-1') as f:
    for line in f:
        track_list.append(line.strip())

track_not_found=[]
for item in track_list:
    found_track=0
    search_results = ytmusic.search(item,filter='songs')
    for idx in range(len(search_results)):
        artist=search_results[idx]['artists'][0]['name']
        title=search_results[idx]['title'] 
        if item.find(artist)!=-1 and item.find(title)!=-1:
            print("Adding: "+item)
            found_track=1
            ytmusic.add_playlist_items(playlistId, [search_results[idx]['videoId']]) 
            break
    if found_track==0:
        print("Not found: "+item)
        track_not_found.append(item)
f = open('tracks_not_found.txt', 'a')
f.write("----"+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\n")
for item in track_not_found:
    f.write(item+"\n")
f.close()

