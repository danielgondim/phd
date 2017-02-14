import requests, sys, acoustic_brainz, music_brainz, time, datetime, calendar

from unidecode import unidecode

API_KEY = sys.argv[1]
LASTFM_USERNAME = "felipevf" 
LIMIT_OF_MUSICS = "10"
TIMESTAMP_DIFFERENCE = 14400
INITIAL_TIME = str(int(time.time()) - 3600)
FINAL_TIME = str(int(time.time()))
API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&limit=" + LIMIT_OF_MUSICS
API_REST_LASTFM_TIME = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&from=" + INITIAL_TIME + "&to=" + FINAL_TIME

def is_weekend(date):
	return date.weekday() >= 5 

def convert_to_datetime(date):
	return datetime.datetime.strptime(date + " 00:00:00", "%Y-%m-%d %H:%M:%S")

def api_rest_with_timestamp(date_time):
	timestamp = calendar.timegm(date_time.utctimetuple())
	return "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&from=" + str(timestamp) + "&to=" + \
	str(timestamp + TIMESTAMP_DIFFERENCE)

current_date = convert_to_datetime(sys.argv[2])
current_date += datetime.timedelta(hours=11)
final_date = convert_to_datetime(sys.argv[3])
final_date += datetime.timedelta(hours=11)

while (current_date <= final_date):
	if (current_date.weekday() < 5):
		#pegar musicas pela manha
		print "Musicas da manha do dia: " + str(current_date)
		print api_rest_with_timestamp(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		print data

		print "################################"

		#musicas da tarde
		current_date += datetime.timedelta(hours=6)
		print api_rest_with_timestamp(current_date)
		print "Musicas da tarde do dia: " + str(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		print data

		print "################################"

		#passando para o inicio do expediente do outro dia
		current_date += datetime.timedelta(hours=18)
	else:
		#se for fds passa o dia
		print "Hoje eh fim de semana, nao teve trabalho!!!!"
		print "################################"
		current_date += datetime.timedelta(days=1)

'''
response = requests.get(API_REST_LASTFM)
data = response.json()

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
	else:
		print "MBID not retrieved"
	print "###########################################"
'''