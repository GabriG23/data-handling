# Esercizio: Combinare intervalli in una fetta “Other”
# Osservando il grafico della Figura 8-7, si può notare che alcuni intervalli sono rappresentati
# da una fetta molto sottile della torta. Questi sono gli intervalli con un numero di dipendenti
# pari a uno o due. Modificate il grafico in modo che questi intervalli siano uniti in un’unica
# fetta etichettata Other. A tal fine, è necessario modificare l’array count e la lista labels.
# Quindi, si deve ricreare il grafico.
import numpy as np
from matplotlib import pyplot as plt

def piechart():
    salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324,
            1326, 2337, 2346, 1354, 1355, 1354, 1367, 1372, 1375, 1376, 1378,
            1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437,
            1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522,
            1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]

    count, bins = np.histogram(salaries, bins=np.arange(1100, 1900, 50))
    labels = ['$'+str(bins[i])+'-'+str(bins[i+1]) for i in range(len(bins)-1)]
    non_zero_pos = [i for i, x in enumerate(count) if x != 0] # rimuove le classi con 0 occorrenze
    labels = [labels[i] for i in non_zero_pos]
    count = [count[i] for i in non_zero_pos]

    new_counts = [] # creo due nuove strutture per separare i valori normali dagli "other" con 1 o 2 dipendenti
    new_labels = []
    other_total = 0

    for i, c in enumerate(count):
        if c <= 2:
            other_total += c
        else:
            new_counts.append(c)
            new_labels.append(labels[i])

    if other_total > 0: # aggiunta di other
        new_counts.append(other_total)
        new_labels.append("Other")

    # Creazione del grafico a torta
    plt.pie(new_counts, labels=new_labels, autopct='%1.1f%%')
    plt.title('Monthly Salaries in the Sales Department')
    plt.savefig("images/esercizio1_torta.png", dpi=300)
    plt.show()

if __name__ == '__main__':
    piechart()