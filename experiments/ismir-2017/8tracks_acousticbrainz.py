#-*- coding:utf-8 -*-
#!/usr/bin/python
import MySQLdb
import musicbrainz, acousticbrainz, json

def retrieve_mbid_and_tags(song_name, artist_name):
	MBIDs = musicbrainz.retrieveMBID(song_name, artist_name)
	if len(MBIDs) > 0:
		for id in MBIDs:
			acoustic_tags = acousticbrainz.retrieveHighLevelFeatures(id)
			if acoustic_tags != {}:
				data_to_return = {}
				for tag in acoustic_tags['highlevel']:
					if tag.startswith('mood') or tag.startswith('genre'):
						data_to_return[tag] = {}
						for sub_tag in acoustic_tags['highlevel'][tag]:
							if not sub_tag.startswith('ve'):
								data_to_return[tag][sub_tag] = acoustic_tags['highlevel'][tag][sub_tag]
				return data_to_return
	return {}

db = MySQLdb.connect(host="localhost",    
                     user="root",         
                     passwd="yourPassword",  
                     db="8_tracks",       
                     charset="utf8",
                     use_unicode=True)     

cur = db.cursor()

query = "SELECT M.user_id, MT.mix_id, M.name, M.tag_list_cache, M.mixes_tracks_count, MT.track_id, T.name, T.performer FROM 8_tracks.mixes AS M, 8_tracks.mixes_tracks AS MT, 8_tracks.tracks AS T WHERE (M.id = MT.mix_id AND MT.track_id = T.id) ORDER BY MT.mix_id LIMIT 0,10;"

cur.execute(query)

data = {'playlists':[]}

playlists_count = 0

current_row = cur.fetchmany()
while current_row != ():
	print 'Nova Playlist:'
	current_playlist = {'user_id':current_row[0][0]}
	current_playlist['playlist_id'] = current_row[0][1]
	current_playlist_id = current_row[0][1]
	current_playlist['playlist_name'] = current_row[0][2]
	current_playlist['textual_tags'] = current_row[0][3]
	current_playlist['number_of_tracks'] = current_row[0][4]
	current_playlist['tracks'] = []
	while (current_row[0][1] == current_playlist_id):
		print current_row
		current_track = {'8tracks_id':current_row[0][5]}
		current_track['track_name'] = current_row[0][6]
		current_track['artist_name'] = current_row[0][7]
		current_track['acousticbrainz_tags'] = retrieve_mbid_and_tags(current_track['track_name'], current_track['artist_name'])
		current_playlist['tracks'].append(current_track)
		current_row = cur.fetchmany()
		if (current_row == ()):
			break
	data['playlists'].append(current_playlist)
	playlists_count += 1

with open('8tracks_with_acousticbrainz.json', 'w') as outfile:
    json.dump(data, outfile)

file = open('playlists_count_8tracks.txt', 'w')
file.write(str(playlists_count))
file.close()