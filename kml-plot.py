import sys
import matplotlib
import numpy as np
import math
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as ppl
from pylab import rcParams
import simplekml
import scipy.interpolate
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker

# Filename of the scan - read as the user input
filename = sys.argv[1]
name = filename[:-4]

# Read data
data = np.genfromtxt(filename, delimiter=',')
# Copy coordinates and radio signal
lat = data[:,9]
lon = data[:,10]
signal = data[:,7]

# Interpolate data on the grid
X, Y = np.linspace(lon.min(), lon.max(), 500), np.linspace(lat.min(), lat.max(), 500)
X, Y = np.meshgrid(X, Y)
Z = scipy.interpolate.griddata((lon, lat), signal, (X, Y), method='linear')

# Color plot
rcParams['figure.figsize'] = (8,8)
fig1 = ppl.figure(1)
ax1 = fig1.add_axes([0,0,1,1])
ax1.axis('off')
surf = ppl.pcolor(X, Y, Z, cmap='jet', vmin=-120, vmax=-40)
ppl.axis('off')
# Get borders
border1 = ppl.axis()
if False:
    ppl.show()
else:
    pngName1 = name + '-Overlay.png'
    fig1.savefig(pngName1, transparent=True)

bottomleft1  = (border1[0],border1[2])
bottomright1 = (border1[1],border1[2])
topright1    = (border1[1],border1[3])
topleft1     = (border1[0],border1[3])

# Scatter plot
fig2 = ppl.figure(2)
ax2 = fig2.add_axes([0,0,1,1])
ax2.axis('off')
ax2.scatter(lon, lat, s=50, c=signal, cmap='jet', vmin=-120, vmax=-40)
ppl.axis('off')
# Get borders
border2 = ppl.axis()
if False:
    ppl.show()
else:
    pngName2 = name + '-OverlayScatter.png'
    fig2.savefig(pngName2, transparent=True)

bottomleft2  = (border2[0],border2[2])
bottomright2 = (border2[1],border2[2])
topright2    = (border2[1],border2[3])
topleft2     = (border2[0],border2[3])

# Create kml file with two layers
kml = simplekml.Kml()
ground = kml.newgroundoverlay(name='Map')
ground.icon.href = pngName1
ground.gxlatlonquad.coords =[bottomleft1, bottomright1, topright1, topleft1]
scat = kml.newgroundoverlay(name='Scatter')
scat.icon.href = pngName2
scat.gxlatlonquad.coords =[bottomleft2, bottomright2, topright2, topleft2]
kml.save(name + ".kml")

# Color plot with colorbar
fig3 = ppl.figure(3)
ax3 = fig3.add_subplot(111)
surf = ppl.pcolor(X, Y, Z, cmap='jet', vmin=-120, vmax=-40)
divider = make_axes_locatable(ax3)
cbar = fig3.colorbar(surf, orientation="vertical")
x_labels = ax3.get_xticks()
ax3.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
y_labels = ax3.get_yticks()
ax3.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
ax3.set_xlabel('Longitude')
ax3.set_ylabel('Latitude')

fig3.savefig(name+'.png', transparent=False)
