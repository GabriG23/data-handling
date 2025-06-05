import pandas as pd

def load_data():
    orders = [(9423517, '2022-02-04', 9001),
              (4626232, '2022-02-04', 9003),
              (9423534, '2022-02-04', 9001),
              (9423679, '2022-02-05', 9002),
              (4626377, '2022-02-05', 9003),
              (4626412, '2022-02-05', 9004),
              (9423783, '2022-02-06', 9002),
              (4626490, '2022-02-06', 9004)]
    
    details = [(9423517, 'Jeans', 'Rip Curl', 87.0, 1),
               (9423517, 'Jacket', 'The North Face', 112.0, 1),
               (4626232, 'Socks', 'Vans', 15.0, 1),
               (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
               (9423534, 'Socks', 'DC', 10.0, 2),
               (9423534, 'Socks', 'Quiksilver', 12.0, 2),
               (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
               (4626377, 'Hoody', 'Animal', 44.0, 1),
               (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
               (4626412, 'Shirt', 'Volcom', 78.0, 1),
               (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
               (9423783, 'Shorts', 'Globe', 26.0, 1),
               (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
               (4626490, 'Sweater', 'Dickies', 56.0, 1)]

    df_details = pd.DataFrame(details, columns =['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])
    df_orders = pd.DataFrame(orders, columns =['OrderNo', 'Date', 'Empno'])
    
    emps = [(9001, 'Jeff Russell', 'LA'),
            (9002, 'Jane Boorman', 'San Francisco'),
            (9003, 'Tom Heints', 'NYC'),
            (9004, 'Maya Silver', 'Philadelphia')]
    df_emps = pd.DataFrame(emps, columns =['Empno', 'Empname', 'Location'])
    
    locations = [('LA', 'West'),
                 ('San Francisco', 'West'),
                 ('NYC', 'East'),
                 ('Philadelphia', 'East')]
    df_locations = pd.DataFrame(locations, columns =['Location', 'Region'])
    return df_orders, df_details, df_emps, df_locations

def combination(df_orders, df_details, df_emps, df_locations):
    df_sales = df_orders.merge(df_details)
    return df_sales
'''
Esercizio 10 La presenza di righe per i totali in un DataFrame consente di utilizzarlo come report senza 
dover aggiungere ulteriori passaggi. Tuttavia, se si intende utilizzare il DataFrame in ulteriori
operazioni di aggregazione, potrebbe essere necessario escludere le righe per i totali.
Provate a filtrare il DataFrame df_totals creato nella sezione precedente, escludendo le 
righe del totale generale e del subtotale. Utilizzate le tecniche di slicing discusse in questo capitolo.
'''
if __name__ == '__main__':
    df_orders, df_details, df_emps, df_locations = load_data()
    df_sales = combination(df_orders, df_details, df_emps, df_locations)
    df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
    df_sales = df_sales[['Date','Empno','Total']] # Per filtrare il DataFrame fino alle colonne necessarie, occorre passare una lista dei nomi delle colonne all’operatore [] del DataFrame, come mostrato qui:

    df_sales_emps = df_sales.merge(df_emps)
    df_result = df_sales_emps.merge(df_locations)
    df_result = df_result[['Date','Region','Total']]
    df_date_region = df_result.groupby(['Date','Region']).sum()

    ps = df_date_region.sum(axis = 0)   # Aggiungere un totale generale - sum restituisce una series pandas con la somma sulal colonna total
    ps.name=('All','All')               # il primo all si riferisce alla componente date delal chiave mentre il secondo alla Region

    df_date_region_total = pd.concat([df_date_region, ps.to_frame().T])
    df_totals = []    # aggiungere totali parziali

    for date, date_df in df_date_region.groupby(level=0):
        df_totals.append(date_df)  # aggiunge le righe esistenti
        ps = date_df.sum(axis=0)
        ps.name = (date, 'All')  # MultiIndex (data, 'All')
        df_totals.append(ps.to_frame().T)  # aggiunge la riga di somma

    # Unisce tutto in un unico DataFrame
    df_totals = pd.concat(df_totals)
    
    # l'esercizio parte da qui
    
    # Slicing solo sulle righe che hanno una regione specifica (esclude 'All')
    df_totals = df_totals.sort_index() # va ordinato per fare lo slicing a più livelli
    df_filtered = df_totals.loc[(slice(None), slice('East', 'West')), :]

    print(df_filtered)
