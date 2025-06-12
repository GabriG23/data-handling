# Esercizio : Definire due o più poligoni
# Nella sezione precedente è stato utilizzato un singolo poligono che copre un’area della
# mappa. Provate ora a definire due o più poligoni che coprono aree urbane adiacenti divise
# da un ostacolo come un fiume. Ottenete le coordinate di questi poligoni utilizzando la mappa
# Google della vostra città o di qualsiasi altra area urbana del pianeta. Servono anche le
# coordinate di diversi punti all’interno di questi poligoni per simulare la posizione di alcuni
# taxi e di un punto di raccolta.
# Nello script, definite i poligoni con Shapely e raggruppateli in un dizionario, quindi raggruppate
# i punti che rappresentano i taxi in un altro dizionario. Successivamente, dividete i taxi
# in gruppi in base al poligono in cui si trovano. Questo può essere realizzato utilizzando due
# cicli: uno esterno per iterare sui poligoni e uno interno per iterare sui punti che rappresentano
# i taxi, controllando se un punto si trova all’interno di un poligono a ogni iterazione del
# ciclo interno. Il seguente frammento di codice illustra come potrebbe essere implementato:

'''
cabs_dict = {}
polygons = {'poly1': poly1, 'poly2': poly2}
cabs = {'cab_26': cab_26, 'cab_112': cab_112}
for poly_name, poly in polygons.items():
    cabs_dict[poly_name] = []
    for cab_name, cab in cabs.items():
        if cab.within(poly):
            cabs_dict[poly_name].append(cab_name)
'''
# Successivamente, dovete determinare quale poligono contiene il punto di prelievo. Una
# volta che lo conoscete, potete selezionare la lista di taxi corrispondente dal dizionario cabs_
# dict utilizzando il nome del poligono come chiave. Infine, utilizzate geopy per determinare
# quale taxi all’interno del poligono scelto è più vicino al luogo di prelievo.

from shapely.geometry import Point, Polygon
from geopy.distance import distance

def find_taxi():
    # Definizione dei due poligoni (es. due aree urbane adiacenti)
    # POLIGONI IN PARCO DORA, dove abbiamo un fiume
    poly1_coords = [(45.091089, 7.661662), (45.089504, 7.663975), (45.087425, 7.656950)]
    #poligono che prende tutto il corso svizzera, passa il fiume e arriva allo sporting dora
    poly2_coords = [(45.093088, 7.655675), (45.086470, 7.656213), (45.093096, 7.662870)]
    # questa area copre la parte nord di via nole, forma un'altro triangolo sopra a quello di sotto in poly 1
    poly1 = Polygon(poly1_coords)
    poly2 = Polygon(poly2_coords)

    polygons = {'Area1': poly1, 'Area2': poly2}

    cabs = { # TAXI IN CORSO SVIZZERA
        'cab_1': Point(45.089800, 7.660000),
        'cab_2': Point(45.087500, 7.657000),
        'cab_3': Point(45.092583, 7.662867),
        'cab_4': Point(45.091144, 7.662942),
    }

    # Punto di prelievo: all'uscita di AGM, Via nole
    pick_up = Point(45.091809, 7.659888) # dovrebbe stare nell'area 2

    cabs_dict = {} # divido i taxi per area
    for poly_name, poly in polygons.items():
        cabs_dict[poly_name] = []
        for cab_name, cab in cabs.items():
            if cab.within(poly):
                cabs_dict[poly_name].append(cab_name)

    pickup_area = None  # in quale area non si trova il punto di prelievo
    for poly_name, poly in polygons.items():
        if pick_up.within(poly):
            pickup_area = poly_name
            break

    if pickup_area: # calcolo da dsitanza minimia dal punto di prelievo
        print(f"Punto di prelievo si trova in: {pickup_area}")
        nearest_cab = None
        min_dist = float('inf')
        for cab_name in cabs_dict[pickup_area]:
            cab_point = cabs[cab_name]
            dist = distance((pick_up.x, pick_up.y), (cab_point.x, cab_point.y)).m
            if dist < min_dist:
                min_dist = dist
                nearest_cab = cab_name
        print(f"Taxi più vicino: {nearest_cab} a {round(min_dist)} metri")
    else:
        print("Il punto di prelievo non si trova in nessun'area definita.")

if __name__ == '__main__':
    find_taxi()
