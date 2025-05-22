'''
Esercizio 2: Gestione di un inventario di prodotti con pandas Series e Dataframe.
- Crea tre Series pandas distinte: una per nomi dei prodotti (nomi_prodotti), una per i codici prodotto (codici_prodotti) e una per le quantità disponibili in magazzino (quantità_disponibili).
- Utilizza i codici prodotto come indici per le Series(index=[codice1, codice2, ...])
- Combina queste tre Series in un unico DataFrame chiamato inventario_prodotti, assicurandoti che i nomi delle colonne siano chiari (es. 'Nome Prodotto', 'Quantità')
- Accedi e stampa la quantità disponibile per un prodotto specifico utilizzando il suo codice prodotto (indice) e anche utilizzando la sua posizione.
'''
import pandas as pd

def series_creation():
    print("Creazioned della serie di prodotti")
    nomi_prodotti = ['pasta', 'burro', 'pane', 'banane']
    codici_prodotti = [2312, 321, 42, 212]
    quantità_prodotti = [25, 43, 23, 12]
    ser1 = pd.Series(nomi_prodotti, index=codici_prodotti, name='Product')
    ser2 = pd.Series(codici_prodotti, index=codici_prodotti, name='Code')
    ser3 = pd.Series(quantità_prodotti, index=codici_prodotti, name='Quantity')
    return ser1, ser2, ser3

def series_combination(s1, s2, s3):
    df = pd.concat([s1, s2, s3], axis = 1) # axis = 1, combinazione come colonne
    return df

def quantità_disponibile(df, codice):
    print(f"Verifica la quantità di prodotto dato il codice: {codice}")
    if codice in df.index:
        quantità = df.loc[codice, 'Quantity']
        print(f"Quantità disponibile per il prodotto: {df.loc[codice, 'Product']} è: {quantità}")
    else:
        print("Codice prodotto non trovato")

def quantità_disponibile_posizione(df, posizione):
    try:
        riga = df.iloc[posizione]
        nome_prodotto = riga['Product']
        quantità = riga['Quantity']
        print(f"Quantità disponibile per il prodotto {nome_prodotto} alla posizione {posizione} con quantità {quantità}")
    except IndexError:
        print("Posizione non trovato")

if __name__ == '__main__':
    ser1, ser2, ser3 = series_creation()
    print("\n" + "*"*30 + "\n")
    df = series_combination(ser1, ser2, ser3)
    print(f"Il dataframe è stato creato:\n{df}")
    print("\n" + "*"*30 + "\n")
    quantità_disponibile(df, codice=2312)
    quantità_disponibile_posizione(df, posizione=2)

