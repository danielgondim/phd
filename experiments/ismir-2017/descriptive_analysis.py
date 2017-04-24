from collections import Counter
import glob, os, csv, json

NEW_HEADER = ['user_id','playlist_id','num_of_musics','num_of_musics_with_mbid','danceability','gender','genre_dortmund','genre_electronic','genre_rosamerica','genre_tzanetakis','ismir04_rhythm','mood_acoustic','mood_aggressive','mood_electronic','mood_happy','mood_party','mood_relaxed','mood_sad','moods_mirex','timbre','tonal_atonal','voice_instrumental']
NEW_DIRECTORY = '/home/danielgondim/workspace/phd/experiments/ismir-2017/descriptive_analysis/'

def most_common_value(list):
	counter = Counter(list)
	return counter.most_common()

#Numero de playlists
files = glob.glob("/home/danielgondim/workspace/phd/experiments/ismir-2017/playlists_full_data/*.csv")
print "Numero de Playlists: " + str(len(files))

#distribuicao do numero de musicas
#As caracteristicas mais comuns das musicas
count = 0
all_tags = []
new_content = []
new_content.append(NEW_HEADER)
for file in files:
	count += 1
	num_musics = 0
	num_music_mbid = 0
	current_content = []
	music_features = {'danceability':[],'gender':[],'genre_dortmund':[],'genre_electronic':[],'genre_rosamerica':[],'genre_tzanetakis':[],'ismir04_rhythm':[],'mood_acoustic':[],'mood_aggressive':[],'mood_electronic':[],'mood_happy':[],'mood_party':[],'mood_relaxed':[],'mood_sad':[],'moods_mirex':[],'timbre':[],'tonal_atonal':[],'voice_instrumental':[]}
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		reader.next()
		for row in reader:
			user_id = row[0]
			playlist_id = row[5]
			tags = row[6].split(',')
			num_musics += 1
			if row[9] == "TRUE":
				try:
					num_music_mbid += 1
					music_features['danceability'].append(row[10])
					music_features['gender'].append(row[12])
					music_features['genre_dortmund'].append(row[14])
					music_features['genre_electronic'].append(row[16])
					music_features['genre_rosamerica'].append(row[18])
					music_features['genre_tzanetakis'].append(row[20])
					music_features['ismir04_rhythm'].append(row[22])
					music_features['mood_acoustic'].append(row[24])
					music_features['mood_aggressive'].append(row[26])
					music_features['mood_electronic'].append(row[28])
					music_features['mood_happy'].append(row[30])
					music_features['mood_party'].append(row[32])
					music_features['mood_relaxed'].append(row[34])
					music_features['mood_sad'].append(row[36])
					music_features['moods_mirex'].append(row[38])
					music_features['timbre'].append(row[40])
					music_features['tonal_atonal'].append(row[42])
					music_features['voice_instrumental'].append(row[44])
				except:
					pass
	current_content.append(user_id)
	current_content.append(playlist_id)
	current_content.append(num_musics)
	current_content.append(num_music_mbid)
	current_content.append(most_common_value(music_features['danceability']))
	current_content.append(most_common_value(music_features['gender']))
	current_content.append(most_common_value(music_features['genre_dortmund']))
	current_content.append(most_common_value(music_features['genre_electronic']))
	current_content.append(most_common_value(music_features['genre_rosamerica']))
	current_content.append(most_common_value(music_features['genre_tzanetakis']))
	current_content.append(most_common_value(music_features['ismir04_rhythm']))
	current_content.append(most_common_value(music_features['mood_acoustic']))
	current_content.append(most_common_value(music_features['mood_aggressive']))
	current_content.append(most_common_value(music_features['mood_electronic']))
	current_content.append(most_common_value(music_features['mood_happy']))
	current_content.append(most_common_value(music_features['mood_party']))
	current_content.append(most_common_value(music_features['mood_relaxed']))
	current_content.append(most_common_value(music_features['mood_sad']))
	current_content.append(most_common_value(music_features['moods_mirex']))
	current_content.append(most_common_value(music_features['timbre']))
	current_content.append(most_common_value(music_features['tonal_atonal']))
	current_content.append(most_common_value(music_features['voice_instrumental']))
	new_content.append(current_content)
	for tag in tags:
		new_tag = tag.strip()
		if new_tag != '':
			all_tags.append(tag.strip())

with open(NEW_DIRECTORY + 'descriptive_analysis.csv', 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerows(new_content)

#tags mais comuns nas playlists
print most_common_value(all_tags)
