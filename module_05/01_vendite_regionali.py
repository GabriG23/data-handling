'''
Esercizio 1: Analisi di vendita regionali con Numpy
Immagina di avere i dati di vendita trimestrali per tre diverse regioni (Nord, Centro, Sud) su un periodo di quattro trimestri.
Crea un array numpy 2D che rappresenti queste vendite.
Ad esempio: vendite_regionali=np.array([[v_n_t1, v_n_t2, v_n_t3, v_n_t4], [v_c_t1, ..., b_c_t4], [v_s_t1, ..., v_s_t4]])
Utilizza le funzioni statistiche di Numpy per:
- calcolare le vendite totali per ogni regione dell'anno (np.sum() sull'asse appropriato)
- trovare il trimestre con le vendite massime per ogni regione (np.amax() sull'asse appropriato).
- Calcolare le vendite medie per trimestre a livello complessivo (media sull'intero array)
- identificare le vendite minime registrate in qualsiasi trimestre e qualsiasi regione (np.amin() sull'intero array, concettualmente simile a np.max/np.amax)
'''
import numpy as np

REGIONI = ['Nord', 'Sud', 'Centro']
TRIMESTRI = ['T1', 'T2', 'T3', 'T4']

def data_creation():
    #       Nord, Sud, Centro
    #       t1, t2, t3, t4
    print("Creo il dataset delle vendite regionali")
    nord = [100, 400, 300, 900]
    sud = [200, 700, 600, 500]
    centro = [500, 1000, 900, 100]
    data = np.array([nord, sud, centro])
    print (f"Dataset creato:\n{data}")
    return data

def vendite_totali(data):
    print("Vendite totali per ogni regione dell'anno")
    vendite_regione = np.sum(data, axis=1)  # asse orizzontale
    for i, totale in enumerate(vendite_regione):
        print(f"  - {REGIONI[i]}: {totale}")

def vendite_massime(data):
    print("Vendite massime per ogni regione")
    vendite_regione = np.amax(data, axis = 1)
    for i, massimo in enumerate(vendite_regione):
        print(f"  - {REGIONI[i]}: {massimo}")

def vendite_medie_trimestre(data):
    print("Vendite medie per trimestre")
    media = np.mean(data, axis = 0)
    for i, media in enumerate(media):
        print(f"  - {TRIMESTRI[i]}: {media:.2f}")

def vendite_minime_trimestre_regione(data):
    print("Calcolo delle vendite medie per trimestre")
    min = np.amin(data, axis = 0)
    for i, minimo in enumerate(min):
        print(f"  - {TRIMESTRI[i]}: {minimo}")
    min = np.amin(data, axis = 1)
    for i, minimo in enumerate(min):
        print(f"  - {REGIONI[i]}: {minimo}")

if __name__ == '__main__':
    dataset = data_creation()
    print("\n" + "*"*30 + "\n")
    vendite_totali(dataset)
    print("\n" + "*"*30 + "\n")
    vendite_massime(dataset)
    print("\n" + "*"*30 + "\n")
    vendite_medie_trimestre(dataset)
    print("\n" + "*"*30 + "\n")
    vendite_minime_trimestre_regione(dataset)
