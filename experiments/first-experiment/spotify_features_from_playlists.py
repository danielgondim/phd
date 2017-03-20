from spotipy.oauth2 import SpotifyClientCredentials
import spotipy, json

TAGS = ['focus', 'party']
CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json_file_data = {}

for tag in TAGS:
	playlists = sp.search(q=tag, limit=5, type='playlist')
	playlists_informations = [{'playlist_id':data['id'],'owner_id':data['owner']['id']} for data in (playlists['playlists']['items'])]
	features = {'energy':{},'instrumentalness':{},'valence':{},'tempo':{}}
	for playlist in playlists_informations:
		track_list = sp.user_playlist_tracks(playlist['owner_id'], playlist_id=playlist['playlist_id'], fields="items(track(id))")
		for track in track_list['items']:
			try:
				track_id = track['track']['id']
				music_features = sp.audio_features([track_id])
				#music_analysis = sp.audio_analysis(track_id)
				if music_features != {}:
					for feature in features:
						features[feature][track_id] = music_features[0][feature]
			except:
				continue
		print "Fim de uma playlist da tag " + tag
	json_file_data[tag] = features

with open('spotify_features_from_playlists.json', 'w') as outfile:
    json.dump(json_file_data, outfile)

