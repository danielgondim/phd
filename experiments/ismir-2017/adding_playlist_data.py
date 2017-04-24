import glob, os, csv, json

NEW_COLUMNS = ['danceability','gender','genre_dortmund','genre_electronic','genre_rosamerica','genre_tzanetakis','ismir04_rhythm','mood_acoustic','mood_aggressive','mood_electronic','mood_happy','mood_party','mood_relaxed','mood_sad','moods_mirex','timbre','tonal_atonal','voice_instrumental']
NEW_DIRECTORY = '/home/danielgondim/workspace/phd/experiments/ismir-2017/playlists_full_data/'

def retrieve_ab_data(path):
	values = []
	try:
		with open(path) as data_file:
			data = json.load(data_file)
			for information in NEW_COLUMNS:
				values.append(data['highlevel'][information]['value'])
				values.append(data['highlevel'][information]['probability'])
		return values
	except:
		return []

files = glob.glob("*.csv")

count = 0
for file in files:
	count += 1
	new_content = []
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		for column in NEW_COLUMNS:
			header.append(column + '_value')
			header.append(column + '_prob')
		new_content.append(header)
		for row in reader:
			if row[8] == 'TRUE':
				data = retrieve_ab_data(row[7])
				for information in data:
					row.append(information)
			new_content.append(row)
	
	with open(NEW_DIRECTORY + file, 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(new_content)
	print count


