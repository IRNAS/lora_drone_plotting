# lora_drone_plotting
Plotting the data from lora drone mapping

To execute first install basemap. For Windows:

1. Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/
2. Download basemap-1.1.0-cp27-cp27m-win_amd64.whl (or other version)
3. Move file to Python folder
4. cd into folder, do `pip install basemap-1.1.0-cp27-cp27m-win_amd64.whl`

For Linux:
1. Go to Github repository https://github.com/matplotlib/basemap/blob/master/README.md
2. Clone repository and follow installation instructions

All other packages can be installed using pip

Run the code:

`python kml-plot.py <csv file name>`

It will produce:

filename.kml: kml file - open in Google Earth
filename-Overlay.png - overlay colorplot image
filename-OverlayScatter.png - overlay scatterplot image
filename.png - colorplot with colorbar image

Sample file drone-scan-10m-podova-mapper-2dB-gw-2dB.csv and corresponding output files are added in the folder. Run:

`python kml-plot.py drone-scan-10m-podova-mapper-2dB-gw-2dB.csv`

