import csv, glob

files = glob.glob("/home/danielgondim/workspace/project-2017-1/playlists_focus_with_features_v2/*.csv")
files += glob.glob("/home/danielgondim/workspace/project-2017-1/playlists_not_focus_with_features/*.csv")

final_songs = [['user_id','mix_id','mix_name','mix_tags','track_id','track_name','artist_name','focus','voice_instrumental_value','voice_instrumental_prob','bpm','danceability_value','danceability_prob','tone']]

for file in files:
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		for row in reader:
			if len(row) > 8:
				final_songs.append(row)

with open('songs_with_features_v2.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerows(final_songs)