import glob, os, csv, json

NEW_DIRECTORY = '/tmp/playlists_full_data/'

def retrieve_user_id(playlist):
	path = '/local/daniel/playlists/' + playlist
	try:
		with open(path) as data_file:
			data = json.load(data_file)
			return data['user_id']
	except:
		return ''

files = glob.glob("*.csv")

count = 0
for file in files:
	count += 1
	new_content = []
	with open(file, 'rb') as playlist_input:
		reader = csv.reader(playlist_input)
		header = reader.next()
		header.insert(0,'user_id')
		new_content.append(header)
		for row in reader:
			row.insert(0, retrieve_user_id(file[:-4]))
			new_content.append(row)
	
	with open(NEW_DIRECTORY + file, 'w') as output:
		writer = csv.writer(output, lineterminator='\n')
		writer.writerows(new_content)
	print count


