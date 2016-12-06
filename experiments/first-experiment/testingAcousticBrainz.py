import requests, sys, acoustic_brainz, music_brainz, charts, time

from unidecode import unidecode

API_KEY = sys.argv[1]
LASTFM_USERNAME = "danielgem" 
LIMIT_OF_MUSICS = "30"
INITIAL_TIME = str(int(time.time()) - 3600)
FINAL_TIME = str(int(time.time()))
API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&limit=" + LIMIT_OF_MUSICS
#API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	#LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&limit=" + LIMIT_OF_MUSICS + "&from=" + \
	#INITIAL_TIME + "&to=" + FINAL_TIME

def sum_high_level_features(current_features):
	global music_features
	for feature in music_features.keys():
		music_features[feature] = music_features[feature] + current_features[feature]


response = requests.get(API_REST_LASTFM)
data = response.json()

global music_features
music_features = {"mood_electronic":0, "mood_party":0, "mood_aggressive":0, "mood_acoustic":0, "mood_happy":0, "mood_sad":0, "mood_relaxed":0}
musicCount = 0
for track in data['recenttracks']['track']:
	MBIDs = []
	artist = unidecode(track['artist']['#text'])
	song = unidecode(track['name'])
	songMBID = track['mbid']
	musicCount += 1
	print "Retrieving informations about music " + str(musicCount) + " ..."
	if songMBID == '':
		MBIDs = music_brainz.retrieveMBID(song, artist)
	else:
		MBIDs.append(songMBID)
	if len(MBIDs) > 0:
		print "MBID retrieved: " + MBIDs[0]
		high_level_features = acoustic_brainz.retrieveHighLevelFeatures(MBIDs[0])
		if high_level_features != {}:
			print "High level features retrieved"
		else:
			print "High level features not retrieved"
		low_level_features = acoustic_brainz.retrieveLowLevelFeatures(MBIDs[0])
		if low_level_features != {}:
			print "Low level features retrieved"
		else:
			print "Low level features not retrieved"
		#	sum_high_level_features(features)
	print "###########################################"

#print music_features
#charts.pie_chart(music_features)