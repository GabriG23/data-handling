# Esercizio: Disegnare una mappa con Cartopy e Matplotlib
# Ora che sapete come creare una mappa con Cartopy e Matplotlib, create una mappa che
# mostri le città di un’altra località degli Stati Uniti. Ad esempio, potreste creare una mappa
# per la California settentrionale. È necessario specificare valori diversi di latitudine e longitudine
# per gli assi y e x.

# vedere file cartopy.ipynb

'''
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LongitudeFormatter, LatitudeFormatter

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv") # carico le città
calif_north = us_cities[(us_cities.State == 'California') & (us_cities.lat > 37)] # filtro per la california settentrionale
top_cities = calif_north[calif_north['Population'] >= 250000] # solo città con 100k, possiamo anche metterne 250k

fig = plt.figure(figsize=[15, 8]) # creo la mappa da plottare
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines('10m')
ax.set_extent([-124, -120, 37, 41], crs=ccrs.PlateCarree())  # California settentrionale

ax.set_xticks([-124, -123, -122, -121, -120], crs=ccrs.PlateCarree()) # aggiunta della griglia
ax.set_yticks([37, 38, 39, 40, 41], crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

X = top_cities['lon'] # scatter delle città
Y = top_cities['lat']
cities = top_cities['City']

ax.scatter(X, Y, color='blue', marker='o', transform=ccrs.PlateCarree())

for i in top_cities.index: #etichette delle città
    ax.text(X[i], Y[i] + 0.1, cities[i],
            transform=ccrs.Geodetic(), fontsize=10,
            horizontalalignment='center', clip_on=True)

plt.title("Città > 1.000.000 abitanti nella California Settentrionale", fontsize=16)
plt.show()
'''

if __name__ == '__main__':
    print("ciao")