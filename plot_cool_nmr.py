#!/usr/bin/env python

from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, rcParams
import plt_utils


#parse text file and extract data
with open('nmr_data.txt') as fo:
    lines = fo.readlines()

#each row of data is a data point (x,y); data has shape (N,2)
data = np.array([list(map(float, l.rstrip().lstrip().split()))[:2] for l in lines])

plt_utils.setup_tex()
rcParams['font.size'] = 20
plt.style.use('dark_background')

fig, ax = plt.subplots(1,1)
#clrs = plt_utils.get_cm(data[1][1:],'cool',max_val=1)

#this part basically organises the data into a set of segments connecting adjacent data points
pts = data.reshape(-1,1,2)
segments = np.concatenate([pts[:-1], pts[1:]],axis=1)

#this assigns a color (from the color map defined by cmap) to each segment
norm = plt.Normalize(data[:,1].min(),data[:,1].max())
lc = LineCollection(segments,cmap='cool',norm=norm)

#the color of each segment is determined by the y-value of the 2nd point of each segment
lc.set_array(data[1:,1])

#the usual plotting crap
lc.set_linewidth(1.5)
ax.add_collection(lc)
ax.set_xlim(-2.5,14.5)
ax.set_ylim(-50,4700)
ax.tick_params(left=False,labelleft=False)
ax.set_xlabel('$\delta$ (ppm)')

plt.show()
