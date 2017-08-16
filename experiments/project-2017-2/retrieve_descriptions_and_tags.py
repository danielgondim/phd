import MySQLdb
import MySQLdb.cursors
import csv
import cjson
import gzip

conn = MySQLdb.connect(host="localhost",    
					user="root",         
                    passwd="moti1989",  
                    db="8tracks",       
                    charset="utf8",
                    use_unicode=True, 
                    cursorclass = MySQLdb.cursors.SSCursor)

cur = conn.cursor()

cur.execute("SELECT DISTINCT name, description, tag_list_cache FROM 8tracks.mixes;")

count = 1
for row in cur:
	current_playlist = []
	if row[0] != None:
		current_playlist.append(row[0].encode('utf-8'))
	else:
		current_playlist.append('')
	if row[1] != None:
		current_playlist.append(row[1].encode('utf-8'))
	else:
		current_playlist.append('')
	if row[2] != None:
		current_playlist.append(row[2].encode('utf-8'))
	else:
		current_playlist.append('')
	print count
	with open('8tracks_text.csv', 'a') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerow(current_playlist)
	count += 1


with gzip.open('aotm2011_playlists.json.gz', 'r') as file_desc:
    playlists = cjson.decode(file_desc.read())