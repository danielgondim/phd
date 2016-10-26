import requests, urllib2, sys, xmltodict, acoustic_brainz

from unidecode import unidecode

API_KEY = sys.argv[1]
API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=danielgem&api_key=" + API_KEY + "&format=json&limit=1"
API_REST_MUSICBRAINZ = "http://musicbrainz.org/ws/2/recording/?query="

def retrieveMBID(songName, artistName):
	songQuoted = urllib2.quote(songName.replace('/', ''))
	print API_REST_MUSICBRAINZ + songQuoted
	file = urllib2.urlopen(API_REST_MUSICBRAINZ + songQuoted)
	xml = file.read()
	file.close()
	doc = xmltodict.parse(xml)
	listOfRecordings = doc['metadata']['recording-list']['recording']
	listOfMBIDs = []
	for record in listOfRecordings:
		print record['title'].lower()
		print songName.lower()
		print record['title'].lower() in songName.lower()
		print
		if type(record['artist-credit']['name-credit']) == type([]):
			for currentArtist in record['artist-credit']['name-credit']:
				print "dentro do for: " + currentArtist['artist']['name'].lower()
				print "dentro do for: " + artistName.lower()
				if (currentArtist['artist']['name'].lower() in artistName.lower()) and (record['title'].lower() in songName.lower()):
					listOfMBIDs.append(record['@id'])
					break
		else:
			print "fora do for: " + record['artist-credit']['name-credit']['artist']['name'].lower()
			print "fora do for: " + artistName.lower()
			if (record['artist-credit']['name-credit']['artist']['name'].lower() in artistName.lower()) and (record['title'].lower() in songName.lower()):
				listOfMBIDs.append(record['@id'])
	return listOfMBIDs

def retrieveLowLevelFeatures(mbid):
	#recuperar informacoes low-level
	#https://acousticbrainz.org/api/v1/MUSIC-MBID/low-level?n=0
	response = requests.get('https://acousticbrainz.org/api/v1/' + mbid + '/low-level?n=0')
	data = response.json()

	#verificar moods e a probabilidade
	data['high-level']['mood_aggressive']

response = requests.get(API_REST_LASTFM)
data = response.json()

for track in data['recenttracks']['track']:
	MBIDs = []
	artist = track['artist']['#text']
	song = unidecode(track['name'])
	songMBID = track['mbid']
	print "The name of the Artist is: " + artist
	print "The MBID of the Artist is: " + track['artist']['mbid']
	print "The name of the Album is: " + track['album']['#text']
	print "The MBID of the Album is: " + track['album']['mbid']
	print "The name of the Song is: " + song
	print "The MBID of the Song is: " + songMBID + '\n'
	if songMBID == '':
		print 'These are the possibilities of MBIDs for the song "' + song + '"'
		MBIDs = retrieveMBID(song, artist) 
		print MBIDs
	else:
		MBIDs.append(songMBID)
	print '==================================='
	print 'TENTANDO BUSCAR INFORMACOES DO MBID DA MUSICA'
	if len(MBIDs) > 0:
		acoustic_brainz.retrieveHighLevelFeatures(MBIDs[0])


#TODO: Treat songs and artists with special characters

#TODO: Retrieve AcousticBrainz informations of a certain MBID
#To retrieve low-level informations: https://acousticbrainz.org/api/v1/MUSIC-MBID/low-level?n=0
#To retrieve high-level informations: https://acousticbrainz.org/api/v1/MUSIC-MBID/high-level?n=0