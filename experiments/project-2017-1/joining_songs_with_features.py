import csv, glob

files = glob.glob("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/playlists_focus_features_big/*.csv")
files += glob.glob("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/playlists_not_focus_features_big/*.csv")

final_songs = [['user_id','mix_id','mix_name','mix_tags','track_id','track_name','artist_name','focus',
'voice_instrumental_value','instrumental','voice','danceability_value','danceable','not_danceable',
'mood_acoustic_value','acoustic','not_acoustic','mood_aggressive_value','aggressive','not_aggressive',
'mood_party_value','party','not_party','mood_relaxed_value','relaxed','not_relaxed','tone','bpm']]

for file in files:
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		for row in reader:
			if len(row) > 8:
				final_songs.append(row)

with open('songs_with_features_big.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerows(final_songs)