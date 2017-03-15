#chamada python testingAcousticBrainz.py 5eb8bc10d65cbdda3cd096f50081ae3c 2017-01-02 2017-01-31
# -*- coding: utf-8 -*-
import requests, sys, acoustic_brainz, music_brainz, time, datetime, calendar
from unidecode import unidecode
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import string
import re

#UTILIZANDO MUSICBRAINZ + ACOUSTICBRAINZ
'''
API_KEY = sys.argv[1]
LASTFM_USERNAME = "felipevf" 
LIMIT_OF_MUSICS = "10"
TIMESTAMP_DIFFERENCE = 10800 #3 horas
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

musics_with_mbid = 0
musics_without_mbid = 0
number_musics = 0
music_with_analysis = 0
music_without_analysis = 0

while (current_date <= final_date):
	if (current_date.weekday() < 5):
		#pegar musicas pela manha
		print "Musicas da manha do dia: " + str(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		for track in data['recenttracks']['track']:
			number_musics += 1
			MBIDs = []
			artist = unidecode(track['artist']['#text'])
			song = unidecode(track['name'])
			print "Musica: " + track['name']
			print "Artista: " + track['artist']['#text']
			if track['mbid'] == '':
				print "Tentando buscar MBID"
				MBIDs = music_brainz.retrieveMBID(song, artist)
				if len(MBIDs) > 0:
					musics_with_mbid += 1
					print "MBID: " + MBIDs[0]
					if acoustic_brainz.retrieveHighLevelFeatures(MBIDs[0]) != {}:
						music_with_analysis += 1
					else:
						music_without_analysis += 1
				else:
					print "MBID: " + track['mbid']
					musics_without_mbid += 1
			else:
				musics_with_mbid += 1
				print "MBID: " + track['mbid']
				if acoustic_brainz.retrieveHighLevelFeatures(track['mbid']) != {}:
					music_with_analysis += 1
				else:
					music_without_analysis += 1
			print
		print "################################"

		#musicas da tarde
		current_date += datetime.timedelta(hours=6)
		print "Musicas da tarde do dia: " + str(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		for track in data['recenttracks']['track']:
			number_musics += 1
			MBIDs = []
			artist = unidecode(track['artist']['#text'])
			song = unidecode(track['name'])
			print "Musica: " + track['name']
			print "Artista: " + track['artist']['#text']
			if track['mbid'] == '':
				print "Tentando buscar MBID"
				MBIDs = music_brainz.retrieveMBID(song, artist)
				if len(MBIDs) > 0:
					musics_with_mbid += 1
					print "MBID: " + MBIDs[0]
					if acoustic_brainz.retrieveHighLevelFeatures(MBIDs[0]) != {}:
						music_with_analysis += 1
					else:
						music_without_analysis += 1
				else:
					print "MBID: " + track['mbid']
					musics_without_mbid += 1
			else:
				musics_with_mbid += 1
				print "MBID: " + track['mbid']
				if acoustic_brainz.retrieveHighLevelFeatures(track['mbid']) != {}:
					music_with_analysis += 1
				else:
					music_without_analysis += 1
			print
		print "################################"

		#passando para o inicio do expediente do outro dia
		current_date += datetime.timedelta(hours=18)
	else:
		#se for fds passa o dia
		print "Hoje eh fim de semana, nao teve trabalho!!!!"
		print "################################"
		current_date += datetime.timedelta(days=1)

print "Total de musicas com analise acustica: " + str(music_with_analysis)
print "Total de musicas sem analise acustica: " + str(music_without_analysis)
print "Total de musicas com MBID: " + str(musics_with_mbid)
print "Total de musicas sem MBID: " + str(musics_without_mbid)
print "Total de musicas: " + str(number_musics)
'''


API_KEY = sys.argv[1]
LASTFM_USERNAME = "felipevf" 
LIMIT_OF_MUSICS = "10"
TIMESTAMP_DIFFERENCE = 10800 #3 horas
INITIAL_TIME = str(int(time.time()) - 3600)
FINAL_TIME = str(int(time.time()))
API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&limit=" + LIMIT_OF_MUSICS
API_REST_LASTFM_TIME = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&from=" + INITIAL_TIME + "&to=" + FINAL_TIME
CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

def is_weekend(date):
	return date.weekday() >= 5 

def convert_to_datetime(date):
	return datetime.datetime.strptime(date + " 00:00:00", "%Y-%m-%d %H:%M:%S")

def api_rest_with_timestamp(date_time):
	timestamp = calendar.timegm(date_time.utctimetuple())
	return "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&from=" + str(timestamp) + "&to=" + \
	str(timestamp + TIMESTAMP_DIFFERENCE)

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

current_date = convert_to_datetime(sys.argv[2])
current_date += datetime.timedelta(hours=12)
final_date = convert_to_datetime(sys.argv[3])
final_date += datetime.timedelta(hours=12)

musics_with_spotifyid = 0
musics_without_spotifyid = 0
number_musics = 0
music_with_spotify_analysis = 0
music_without_spotify_analysis = 0

while (current_date <= final_date):
	if (current_date.weekday() < 5):
		#pegar musicas pela manha
		print "Musicas da manha do dia: " + str(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		for track in data['recenttracks']['track']:
			music_found = False
			track_id = ""
			number_musics += 1
			print "Musica: " + track['name']
			print "Artista: " + track['artist']['#text']
			string_search = track['name']
			string_search = re.sub('/', ' ', string_search)
			string_search = " ".join(string_search.split())
			#print string_search

			try:
				results = sp.search(q=string_search, limit=50, type='track')
				if len(results["tracks"]["items"]) > 0:
					for item in results["tracks"]["items"]:
						if music_found:
							break
						if item["name"] == string_search:
							for artist in item["artists"]:
								if artist["name"].lower() == track["artist"]["#text"].lower():
									track_id = item["id"]
									print "Spotify ID: " + track_id
									musics_with_spotifyid += 1
									music_found = True
									if sp.audio_features([track_id]) != {}:
										music_with_spotify_analysis += 1
									else:
										music_without_spotify_analysis += 1
									break
				if track_id == "":
					print "Spotify ID:"
					musics_without_spotifyid += 1
			except:
				print "Deu erro mas continuei. Sem Spotify ID!"
				musics_without_spotifyid += 1
				print
				continue
			print
		print "################################"

		#musicas da tarde
		current_date += datetime.timedelta(hours=6)
		print "Musicas da tarde do dia: " + str(current_date)
		response = requests.get(api_rest_with_timestamp(current_date))
		data = response.json()
		for track in data['recenttracks']['track']:
			music_found = False
			track_id = ""
			number_musics += 1
			print "Musica: " + track['name']
			print "Artista: " + track['artist']['#text']
			string_search = track['name']
			string_search = re.sub('/', ' ', string_search)
			string_search = " ".join(string_search.split())
			#print string_search

			try:
				results = sp.search(q=string_search, limit=50, type='track')
				if len(results["tracks"]["items"]) > 0:
					for item in results["tracks"]["items"]:
						if music_found:
							break
						if item["name"] == string_search:
							for artist in item["artists"]:
								if artist["name"].lower() == track["artist"]["#text"].lower():
									track_id = item["id"]
									print "Spotify ID: " + track_id
									musics_with_spotifyid += 1
									music_found = True
									if sp.audio_features([track_id]) != {}:
										music_with_spotify_analysis += 1
									else:
										music_without_spotify_analysis += 1
									break
				if track_id == "":
					print "Spotify ID:"
					musics_without_spotifyid += 1
			except:
				print "Deu erro mas continuei. Sem Spotify ID!"
				musics_without_spotifyid += 1
				print
				continue
			print
		print "################################"

		#passando para o inicio do expediente do outro dia
		current_date += datetime.timedelta(hours=18)
	else:
		#se for fds passa o dia
		print "Hoje eh fim de semana, nao teve trabalho!!!!"
		print "################################"
		current_date += datetime.timedelta(days=1)

print "Total de musicas com analise acustica do Spotify: " + str(music_with_spotify_analysis)
print "Total de musicas sem analise acustica do Spotify: " + str(music_without_spotify_analysis)
print "Total de musicas com ID do Spotify: " + str(musics_with_spotifyid)
print "Total de musicas sem ID do Spotify: " + str(musics_without_spotifyid)
print "Total de musicas: " + str(number_musics)


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