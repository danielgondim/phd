'''import numpy as np
import pylab as p

data=np.array(np.random.rand(1000))
y,binEdges=np.histogram(data,bins=100)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
p.plot(bincenters,y,'-')
p.show()


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import json

with open('spotify_features_from_playlists.json') as data_file:    
    data = json.load(data_file)

print type(data)

values = [feature for feature in data['party']['energy'].values()]
print values

noise = np.random.normal(0, 1, (1000, ))

density = stats.gaussian_kde(values)
n, x, _ = plt.hist(values, bins=np.linspace(0, 1, len(values)), 
                   histtype=u'step', normed=True)  
plt.plot(x, density(x))
plt.set_xlabel('Energy')
plt.set_ylabel('Probability density')
plt.set_title('Histograma de Energia')
plt.show()
'''

import matplotlib, json
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

with open('spotify_features_from_playlists.json') as data_file:    
    data = json.load(data_file)

x = [feature for feature in data['party']['energy'].values()]


# Make a normed histogram. It'll be multiplied by 100 later.
plt.hist(x, bins=50, normed=True)

# Create the formatter using the function to_percent. This multiplies all the
# default labels by 100, making them all percentages
formatter = FuncFormatter(to_percent)

# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)

plt.show()