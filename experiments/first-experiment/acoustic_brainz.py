import requests

def retrieveHighLevelFeatures(mbid):
	#recuperar informacoes high-level
	#https://acousticbrainz.org/api/v1/MUSIC-MBID/high-level?n=0
	response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/high-level?n=0')
	data = response.json()
	try:
		highlevel_content = data['highlevel']
		print "VOICE AND GENDER"
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
		return data['highlevel']
	except KeyError:
		print "No informations to show about this MBID"
		return []

'''highlevel_content = retrieveHighLevelFeatures('716f0fa1-c526-4995-a8ad-ff57c44bf9b1')
print highlevel_content
#30ac9667-bc70-4541-a022-a3a881784ec2
#716f0fa1-c526-4995-a8ad-ff57c44bf9b1


print "VOICE AND GENDER"
print "Voice: " + highlevel_content['voice_instrumental']['value']
print "Gender: " + highlevel_content['gender']['value'] + '\n'

print "MOODS"
print "Electronic: " + highlevel_content['mood_electronic']['value']
print "Party: " + highlevel_content['mood_party']['value']
print "Agressive: " + highlevel_content['mood_aggressive']['value']
print "Acoustic: " + highlevel_content['mood_acoustic']['value']
print "Happy: " + highlevel_content['mood_happy']['value']
print "Sad: " + highlevel_content['mood_sad']['value']
print "Relaxed: " + highlevel_content['mood_relaxed']['value']'''