import requests

moods_list = ['mood_electronic', 'mood_party', 'mood_aggressive', 'mood_acoustic', 'mood_happy', 'mood_sad', 'mood_relaxed']

def mood_translator(value):
	if value.startswith("not_"):
		return 0
	return 1

def retrieveHighLevelFeatures(mbid):
	response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/high-level?n=0')
	data = response.json()
	try:
		highlevel_content = data['highlevel']
		features = {}
		for mood in moods_list:
			features[mood] = mood_translator(highlevel_content[mood]['value'])
		return features
		'''print "VOICE AND GENDER"
		print "Voice: " + highlevel_content['voice_instrumental']['value']
		print "Gender: " + highlevel_content['gender']['value'] + '\n'

		print "MOODS"
		print "Electronic: " + highlevel_content['mood_electronic']['value']
		print "Party: " + highlevel_content['mood_party']['value']
		print "Agressive: " + highlevel_content['mood_aggressive']['value']
		print "Acoustic: " + highlevel_content['mood_acoustic']['value']
		print "Happy: " + highlevel_content['mood_happy']['value']
		print "Sad: " + highlevel_content['mood_sad']['value']
		print "Relaxed: " + highlevel_content['mood_relaxed']['value'] + '\n'
		#return data['highlevel']'''
	except KeyError:
		return {}

def retrieveLowLevelFeatures(mbid):
	#recuperar informacoes low-level
	#https://acousticbrainz.org/api/v1/MUSIC-MBID/low-level?n=0
	response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/low-level?n=0')
	data = response.json()

	#verificar moods e a probabilidade
	data['high-level']['mood_aggressive']