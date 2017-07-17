#-*- coding:utf-8 -*-
#!/usr/bin/python
import MySQLdb
import musicbrainz, acousticbrainz, glob, csv

NEW_COLUMNS = ['focus','voice_instrumental_value','voice_instrumental_prob','bpm','danceability_value','danceability_prob','tone']
NEW_DIRECTORY = '/home/danielgondim/workspace/project-2017-1/playlists_not_focus_with_features/'

def retrieve_features(song_name, artist_name):
	MBIDs = musicbrainz.retrieve_MBID(song_name, artist_name)
	if len(MBIDs) > 0:
		for id in MBIDs:
			highlevel_features = acousticbrainz.retrieve_highlevel_features(id)
			if highlevel_features != {}:
				danceability_prob = highlevel_features['highlevel']['danceability']['probability']
				danceability_value = highlevel_features['highlevel']['danceability']['value']
				voice_instrumental_prob = highlevel_features['highlevel']['voice_instrumental']['probability']
				voice_instrumental_value = highlevel_features['highlevel']['voice_instrumental']['value']
				
				lowlevel_features = acousticbrainz.retrieve_lowlevel_features(id)
				bpm = lowlevel_features['rhythm']['bpm']
				tone = lowlevel_features['tonal']['chords_scale']

				return [voice_instrumental_value,voice_instrumental_prob,bpm,danceability_value,danceability_prob,tone]
	return []

files = glob.glob("/home/danielgondim/workspace/project-2017-1/playlists_not_focus/*.csv")

count = 0
for file in files:
	count += 1
	new_content = []
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		header[3] = 'mix_tags'
		for column in NEW_COLUMNS:
			header.append(column)
		new_content.append(header)
		for row in reader:
			features = [0] + retrieve_features(row[5], row[6])
			for feature in features:
				row.append(feature)
			new_content.append(row)
	with open(NEW_DIRECTORY + file.split('/')[-1], 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(new_content)
	print count