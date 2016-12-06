import urllib2, xmltodict

from unidecode import unidecode

API_REST_MUSICBRAINZ = "http://musicbrainz.org/ws/2/recording/?query="

def retrieveMBID(songName, artistName):
  songQuoted = urllib2.quote(songName.replace('/', ''))
  try:
    file = urllib2.urlopen(API_REST_MUSICBRAINZ + songQuoted)
    xml = file.read()
    file.close()
    doc = xmltodict.parse(xml)
    listOfRecordings = doc['metadata']['recording-list']['recording']
    listOfMBIDs = []
    MBID_found = False

    for record in listOfRecordings:
      if type(record) == unicode:
        if (((unidecode(listOfRecordings['artist-credit']['name-credit']['artist']['name']).lower() in artistName.lower()) or
            (artistName.lower() in unidecode(listOfRecordings['artist-credit']['name-credit']['artist']['name']).lower()))
          and ((unidecode(listOfRecordings['title'].lower()) in songName.lower()) or (songName.lower() in unidecode(listOfRecordings['title'].lower())))):
            listOfMBIDs.append(listOfRecordings['@id'])
            MBID_found = True
        break
      else:
        currentArtistList = record['artist-credit']['name-credit']
        if type(currentArtistList) == type([]):
          for currentArtist in currentArtistList:
            if (((unidecode(currentArtist['artist']['name']).lower() in artistName.lower()) or
                (artistName.lower() in unidecode(currentArtist['artist']['name']).lower()))
              and ((unidecode(record['title'].lower()) in songName.lower()) or (songName.lower() in unidecode(record['title'].lower())))):
              listOfMBIDs.append(record['@id'])
              MBID_found = True
              break
        else:
          if (((unidecode(currentArtistList['artist']['name']).lower() in artistName.lower()) or
              (artistName.lower() in unidecode(currentArtistList['artist']['name']).lower()))
            and ((unidecode(record['title'].lower()) in songName.lower()) or (songName.lower() in unidecode(record['title'].lower())))):
              listOfMBIDs.append(record['@id'])
              MBID_found = True
              break 
      if MBID_found:
        break    
    return listOfMBIDs
  except urllib2.HTTPError:
    return []  