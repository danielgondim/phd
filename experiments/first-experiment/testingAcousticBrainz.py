import pylast, requests, sys

API_KEY = sys.argv[1]
API_REST = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=danielgem&api_key=" + API_KEY + "&format=json&limit=25"

response = requests.get(API_REST)
data = response.json()

for i in data['recenttracks']['track']:
	print "The name of the Artist is: " + i['artist']['#text']
	print "The MBID of the Artist is: " + i['artist']['mbid']
	print "The name of the Album is: " + i['album']['#text']
	print "The MBID of the Album is: " + i['album']['mbid']
	print "The name of the Song is: " + i['name']
	print "The MBID of the Song is: " + i['mbid'] + '\n'

#TODO: If song has no MBID, retrieve it from MusicBrainz (by song name and artist name).

#TODO: Retrieve AcousticBrainz informations of a certain MBID