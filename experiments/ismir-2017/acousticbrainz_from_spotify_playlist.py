from spotipy.oauth2 import SpotifyClientCredentials
import spotipy, json, musicbrainz, acousticbrainz

TAGS = ['beach','winter','working','travel']
CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json_file_data = {}

for tag in TAGS:
	playlists = sp.search(q=tag, limit=2, type='playlist')
	playlists_informations = [{'playlist_id':data['id'],'owner_id':data['owner']['id'],'playlist_name':data['name']} for data in (playlists['playlists']['items'])]
	#features = {'energy':{},'instrumentalness':{},'valence':{},'tempo':{}}
	for playlist in playlists_informations:
		print "Playlist a ser analisada: " + playlist['playlist_name']
		track_list = sp.user_playlist_tracks(playlist['owner_id'], playlist_id=playlist['playlist_id'], fields="items(track(name, artists(name)))")
		number_musics = 0
		music_with_analysis = 0
		music_without_analysis = 0
		for track in track_list['items']:
			#print 'Retrieving informantions of song: ' + track['track']['name']
			number_musics += 1
			for artist in track['track']['artists']:
				MBIDs = musicbrainz.retrieveMBID(track['track']['name'], artist['name'])
				if len(MBIDs) > 0:
					if acousticbrainz.retrieveHighLevelFeatures(MBIDs[0]) != {}:
						music_with_analysis += 1
						break
					else:
						music_without_analysis += 1
		print 'Total de musicas: ' + str(number_musics)
		print 'Total de musicas com analise do acousticbrainz: ' + str(music_with_analysis)
		print 'Total de musicas sem analise do acousticbrainz: ' + str(music_without_analysis)
		print
	print
	print "Fim das playlists da tag " + tag
	print "#########"

print 'Total de musicas: ' + str(number_musics)
print 'Total de musicas com analise do acousticbrainz: ' + str(music_with_analysis)
print 'Total de musicas sem analise do acousticbrainz: ' + str(music_without_analysis)

'''
track_list = sp.user_playlist_tracks('spotify', playlist_id='3J3mTk0N0NzDOFgnp67Z75', fields="items(track(name, artists(name)))")
for track in track_list['items']:
	print 'Retrieving informantions of song: ' + track['track']['name']
	number_musics += 1
	for artist in track['track']['artists']:
		MBIDs = musicbrainz.retrieveMBID(track['track']['name'], artist['name'])
		if len(MBIDs) > 0:
			if acousticbrainz.retrieveHighLevelFeatures(MBIDs[0]) != {}:
				music_with_analysis += 1
				break
			else:
				music_without_analysis += 1

print 'Total de musicas: ' + str(number_musics)
print 'Total de musicas com analise do acousticbrainz: ' + str(music_with_analysis)
print 'Total de musicas sem analise do acousticbrainz: ' + str(music_without_analysis)
'''