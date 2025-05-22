'''
Esercizio 4: Aggregazione e riepilogo di dati di recensioni di film con gropuby()
Immagina di avere un DF recensioni_film con le colonne ID Film, Titolo Film, Punteggio (su una scala da 1 a 5)
Utilizza la funzione groupby() di pandas per:
    - calcolare il punteggio medio per ciascun film
    - contare il numero di totale di recensioni per ciascun film (size() o count() su una colonna)
    - identificare il punteggio massimo e minimo ricevuto da ciascun film
'''
import pandas as pd

def dataset_creation():
    print("Creazione del dataset di recensioni film")
    id_film = [101, 102, 101, 103, 104, 102]
    titoli = ['Matrix', 'Inception', 'Matrix', 'Jurassic Park', 'Signore degli anelli', 'Inception']
    punteggi = [5, 4, 1, 2, 4, 5]
    df = pd.DataFrame({
        'filmID': id_film,
        'Titolo Film': titoli,
        'Punteggio': punteggi
    })
    print(f"Dataset creato:\n{df}")
    return df

def punteggio_medio(df):
    print("Calcolo del punteggio medio per ciascun film")
    media = df.groupby('Titolo Film')['Punteggio'].mean()
    print(media)

def conteggio_recensioni(df):
    print("Conteggio delle recensioni per ciascun film")
    conteggio = df.groupby('Titolo Film')['Punteggio'].count()
    print(conteggio)

def punteggio_max_min(df):
    print("Punteggi massimo e minimo per ciascun film")
    max_min = df.groupby('Titolo Film')['Punteggio'].agg(['max','min'])
    print(max_min)

if __name__ == '__main__':
    recensioni = dataset_creation()
    print("\n" + "*"*30 + "\n")
    punteggio_medio(recensioni)
    print("\n" + "*"*30 + "\n")
    conteggio_recensioni(recensioni)
    print("\n" + "*"*30 + "\n")
    punteggio_max_min(recensioni)


'''
Concetti
- groupby
- aggregate - agg()


'''