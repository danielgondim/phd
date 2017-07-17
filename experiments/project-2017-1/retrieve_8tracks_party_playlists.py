#-*- coding:utf-8 -*-
#!/usr/bin/python
import MySQLdb, csv
#import musicbrainz, acousticbrainz, json

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
                     passwd="moti1989",  
                     db="8tracks",       
                     charset="utf8",
                     use_unicode=True)     

cur = db.cursor()

query = "SELECT M.user_id, MT.mix_id, M.name, M.tag_list_cache, MT.track_id, T.name, T.performer FROM 8tracks.mixes AS M, 8tracks.mixes_tracks AS MT, 8tracks.tracks AS T WHERE (M.id = MT.mix_id AND MT.track_id = T.id AND M.tag_list_cache LIKE '%party%');"

cur.execute(query)

playlists_count = 0

current_row = cur.fetchmany()
while current_row != ():
	current_playlist = []
	header = ['user_id','mix_id','mix_name','mix.tags','track_id','track_name','artist_name']
	current_playlist.append(header)
	user_id = current_row[0][0]
	mix_id = current_row[0][1]
	mix_name = current_row[0][2]
	if mix_name == None:
		mix_name = ''
	else:
		mix_name = mix_name.encode('utf-8')
	mix_tags = current_row[0][3]
	if mix_tags == None:
		mix_tags = ''
	else:
		mix_tags = mix_tags.encode('utf-8')
	while (current_row[0][1] == mix_id):
		track_id = current_row[0][4]
		track_name = current_row[0][5]
		if track_name == None:
			track_name = ''
		else:
			track_name = track_name.encode('utf-8')
		artist_name = current_row[0][6]
		if artist_name == None:
			artist_name = ''
		else:
			artist_name = artist_name.encode('utf-8')
		current_playlist.append([user_id, mix_id, mix_name, mix_tags, track_id, track_name, artist_name])
		current_row = cur.fetchmany()
		if (current_row == ()):
			break
	with open('/home/danielgondim/workspace/project-2017-1/playlists_party/' + str(mix_id) + '.csv', 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(current_playlist)
	playlists_count += 1
	print 'Playlist %d' % playlists_count
	if playlists_count >= 200:
		break