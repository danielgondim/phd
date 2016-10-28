import matplotlib.pyplot as plt

def pie_chart(songs_features):
	labels = songs_features.keys()
	sizes = songs_features.values()
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'silver', 'purple']
	explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

	plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
	plt.axis('equal')
	plt.show()