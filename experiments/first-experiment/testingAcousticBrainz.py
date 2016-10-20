import requests, urllib2, sys, xmltodict

API_KEY = sys.argv[1]
API_REST = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=danielgem&api_key=" + API_KEY + "&format=json&limit=5"

def retrieveMBID(songName, artistName):
	songQuoted = urllib2.quote(songName)
	#print 'http://musicbrainz.org/ws/2/recording/?query=' + songQuoted
	file = urllib2.urlopen('http://musicbrainz.org/ws/2/recording/?query=' + songQuoted)
	xml = file.read()
	file.close()
	doc = xmltodict.parse(xml)
	listOfRecordings = doc['metadata']['recording-list']['recording']
	listOfMBIDs = []
	for record in listOfRecordings:
		if type(record['artist-credit']['name-credit']) == type([]):
			for currentArtist in record['artist-credit']['name-credit']:
				if currentArtist['artist']['name'].lower() == artistName.lower():
					listOfMBIDs.append(record['@id'])
					break
		else:
			if record['artist-credit']['name-credit']['artist']['name'].lower() == artistName.lower():
				listOfMBIDs.append(record['@id'])
	return listOfMBIDs

response = requests.get(API_REST)
data = response.json()

for track in data['recenttracks']['track']:
	artist = track['artist']['#text']
	song = track['name']
	songMBID = track['mbid']
	print "The name of the Artist is: " + artist
	print "The MBID of the Artist is: " + track['artist']['mbid']
	print "The name of the Album is: " + track['album']['#text']
	print "The MBID of the Album is: " + track['album']['mbid']
	print "The name of the Song is: " + song
	print "The MBID of the Song is: " + songMBID + '\n'
	if songMBID == '':
		print 'These are the possibilities of MBIDs for the song "' + song + '"'
		print retrieveMBID(song, artist)
	print '==================================='

#TODO: Retrieve AcousticBrainz informations of a certain MBID
#To retrieve low-level informations: https://acousticbrainz.org/api/v1/MUSIC-MBID/low-level?n=0
#To retrieve high-level informations: https://acousticbrainz.org/api/v1/MUSIC-MBID/high-level?n=0