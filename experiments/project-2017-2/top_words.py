import csv, operator, nltk

top_words = {}

count = 1
with open('8tracks_text.csv', 'rb') as playlist_input:
	reader = csv.reader(playlist_input)
	for row in reader:
		print count
		for column in row:
			tokens = nltk.word_tokenize(column.decode(encoding='UTF-8',errors='strict').lower())
			words = nltk.pos_tag(tokens)
			for word in words:
				if word[1].startswith('NN') or word[1].startswith('VB'):
					if word[0] in top_words:
						top_words[word] += 1
					else:
						top_words[word] = 1
		count += 1

sorted_words = sorted(top_words.items(), key=operator.itemgetter(1), reverse=True)

with open('top_words_nltk.csv','wb') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['word','total'])
    for row in sorted_words:
        csv_out.writerow(row)