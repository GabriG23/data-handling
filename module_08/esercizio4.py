# Esercizio : Migliorare l’algoritmo di prelievo
# Nello script appena discusso, sono stati elaborati i dati di localizzazione relativi a un singolo
# taxi per determinare la distanza tra questo taxi e il luogo di prelievo. Modificate lo script in
# modo che possa determinare le distanze tra il luogo di prelievo e ciascuno dei diversi taxi.
# È necessario raggruppare i punti che rappresentano i taxi in una lista e quindi elaborare
# questa lista in un ciclo, utilizzando l’istruzione if/else dello script precedente come corpo
# del ciclo. Quindi individuate il taxi più vicino al luogo di ritiro.

from shapely.geometry import Point, Polygon
from geopy.distance import distance

def prelievo():
    coords = [(46.082991, 38.987384), (46.075489, 38.987599), # area urbana
              (46.079395, 38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]
    poly = Polygon(coords)

    taxis = {'cab_1': Point(46.073852, 38.991890),
             'cab_2': Point(46.076300, 38.989000),
             'cab_3': Point(46.080200, 38.997500),
             'cab_4': Point(46.083000, 38.993000),}


    pick_up = Point(46.080074, 38.991289)   # punto di prelievo
    entry_point = Point(46.075357, 39.000298)   # punto di entrata

    min_dist = float('inf')     # calcolo per il taxi più vicino
    nearest_cab = None

    for cab_name, cab in taxis.items():
        if cab.within(poly):
            dist = distance((pick_up.x, pick_up.y), (cab.x, cab.y)).m
        else:
            dist = distance((cab.x, cab.y), (entry_point.x, entry_point.y)).m + distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m

        print(f"{cab_name} → distanza: {round(dist)} m")

        if dist < min_dist:
            min_dist = dist
            nearest_cab = cab_name

    print(f"\nIl taxi più vicino è {nearest_cab} a {round(min_dist)} metri")

if __name__ == '__main__':
    prelievo()
