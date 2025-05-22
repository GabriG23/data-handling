'''
Esercizio 3: Unione di dati clienti con diverse politiche di join
Crea un dataframe clienti con le colonne 'ID Cliente', 'Nome', 'Città' per alcuni clienti. Assicurati che l'ID Cliente sia l'indice.
Crea un secondo DataFrame ordini con le colonne 'ID Ordine', 'ID Cliente', 'Importo'. Assicurati che alcuni 'ID Cliente' nel DataFrame ordini corrispondano a quelli nel DF clienti, ma includi anche:
    * un ID Cliente nel DF clienti che NON abbia ordini nel DF ordini
    * un ID cliente nel DF ordini che NON esista nel DF clienti (simulando un errore o un cliente non registrato).
Utilizza i metodi di unione di pandas (join o merge) per combinare i due DataFrame in modo da ottenere:
    * un DataFrame che includa solo gli ordini per i quali esiste un cliente corrispondente nel DF clienti (equivalente a una inner join basata sull'ID Cliente)
    * un DataFrame che includa tutti i clienti dal DataFrame clienti e i loro ordini corrispondenti, mostrando valori mancanti (NaN) per i clienti senza ordini (equivalente a una left join).
    * un DataFrame che includa tutti gli ordini e i dati del cliente corrispondente, mostrando valori mancanti per gli ordini senza un cliente registrato (equivalente a una right join)
'''
import pandas as pd

def dataset_creation_clienti():
    clienti = [432, 12, 553, 331, 211]
    nomi = ['Bruno', 'Donato', 'Mirko', 'Santos', 'Creed']
    citta = ['Milano', 'Torino', 'Milano', 'Torino', 'Roma']
    df_clienti = pd.DataFrame({''
                        'Nome': nomi,
                        'Città': citta
                        }, index=clienti)

    df_clienti.index.name = 'ClientID'
    return df_clienti

def dataset_creation_ordini():
    clienti = [432, 12, 553, 331, 8888]
    ordini = [311, 2039, 23094, 395, 532]
    importi = [100, 200, 300, 100, 500]
    df_ordini = pd.DataFrame({
        'OrderID': ordini,
        'ClientID': clienti,
        'Importo': importi
    })
    return df_ordini 

def inner_join(df_clienti, df_ordini):
    # un DataFrame che includa solo gli ordini per i quali esiste un cliente corrispondente nel DF clienti (equivalente a una inner join basata sull'ID Cliente)
    return pd.merge(df_ordini, df_clienti, on='ClientID', how='inner')

def left_join(df_clienti, df_ordini):
    #  un DataFrame che includa tutti i clienti dal DataFrame clienti e i loro ordini corrispondenti, mostrando valori mancanti (NaN) per i clienti senza ordini (equivalente a una left join).
    return pd.merge(df_clienti, df_ordini, on='ClientID', how='left')

def right_join(df_clienti, df_ordini):
    # un DataFrame che includa tutti gli ordini e i dati del cliente corrispondente, mostrando valori mancanti per gli ordini senza un cliente registrato (equivalente a una right join)
    return pd.merge(df_clienti, df_ordini, on='ClientID', how='right')

if __name__ == '__main__':
    print("Creazione dei dataframe\n")
    df1 = dataset_creation_clienti()
    df2 = dataset_creation_ordini()
    print("Visualizzazione dei df\n")
    print(f"Dataframe clienti:\n {df1}")
    print(f"Dataframe ordini:\n {df2}")
    print(f"Inner join tra i due dataframe:\n{inner_join(df1, df2)}")
    print(f"Left join tra i due dataframe:\n{left_join(df1, df2)}")
    print(f"Right join tra i due dataframe:\n{right_join(df1, df2)}")
