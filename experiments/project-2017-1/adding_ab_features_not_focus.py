#-*- coding:utf-8 -*-
#!/usr/bin/python
import MySQLdb
import musicbrainz, acousticbrainz, glob, csv

NEW_COLUMNS = ['focus','voice_instrumental_value','instrumental','voice','danceability_value','danceable',
'not_danceable','mood_acoustic_value','acoustic','not_acoustic','mood_aggressive_value','aggressive',
'not_aggressive','mood_party_value','party','not_party','mood_relaxed_value','relaxed','not_relaxed','tone','bpm']
NEW_DIRECTORY = '/home/danielgondim/workspace-new/phd/experiments/project-2017-1/playlists_not_focus_features_big/'

def retrieve_features(song_name, artist_name):
	MBIDs = musicbrainz.retrieve_MBID(song_name, artist_name)
	if len(MBIDs) > 0:
		for id in MBIDs:
			highlevel_features = acousticbrainz.retrieve_highlevel_features(id)
			if highlevel_features != {}:
				danceable = highlevel_features['highlevel']['danceability']['all']['danceable']
				not_danceable = highlevel_features['highlevel']['danceability']['all']['not_danceable']
				danceability_value = highlevel_features['highlevel']['danceability']['value']

				instrumental = highlevel_features['highlevel']['voice_instrumental']['all']['instrumental']
				voice = highlevel_features['highlevel']['voice_instrumental']['all']['voice']
				voice_instrumental_value = highlevel_features['highlevel']['voice_instrumental']['value']

				acoustic = highlevel_features['highlevel']['mood_acoustic']['all']['acoustic']
				not_acoustic = highlevel_features['highlevel']['mood_acoustic']['all']['not_acoustic']
				mood_acoustic_value = highlevel_features['highlevel']['mood_acoustic']['value']

				aggressive = highlevel_features['highlevel']['mood_aggressive']['all']['aggressive']
				not_aggressive = highlevel_features['highlevel']['mood_aggressive']['all']['not_aggressive']
				mood_aggressive_value = highlevel_features['highlevel']['mood_aggressive']['value']

				party = highlevel_features['highlevel']['mood_party']['all']['party']
				not_party = highlevel_features['highlevel']['mood_party']['all']['not_party']
				mood_party_value = highlevel_features['highlevel']['mood_party']['value']

				relaxed = highlevel_features['highlevel']['mood_relaxed']['all']['relaxed']
				not_relaxed = highlevel_features['highlevel']['mood_relaxed']['all']['not_relaxed']
				mood_relaxed_value = highlevel_features['highlevel']['mood_relaxed']['value']
				
				lowlevel_features = acousticbrainz.retrieve_lowlevel_features(id)
				bpm = lowlevel_features['rhythm']['bpm']
				tone = lowlevel_features['tonal']['chords_scale']

				return [voice_instrumental_value,instrumental,voice,danceability_value,danceable,not_danceable,
				mood_acoustic_value,acoustic,not_acoustic,mood_aggressive_value,aggressive,not_aggressive,
				mood_party_value,party,not_party,mood_relaxed_value,relaxed,not_relaxed,tone,bpm]
	return []

files = glob.glob("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/playlists_not_focus/*.csv")

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