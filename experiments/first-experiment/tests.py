import json

with open('spotify_features_from_playlists.json') as data_file:    
    data = json.load(data_file)

x = [feature for feature in data['party']['energy'].values()]
file = open('numeros.txt', 'w')
for i in x:
    file.write(str(i)+'\n')
file.close()