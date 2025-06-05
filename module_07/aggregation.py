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

if __name__ == '__main__':
    df_orders, df_details, df_emps, df_locations = load_data()
    print("Dati caricati\n")
    df_sales = combination(df_orders, df_details, df_emps, df_locations)
    print(df_sales)
    df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
    
    # Per filtrare il DataFrame fino alle colonne necessarie, occorre passare una lista dei nomi delle colonne all’operatore [] del DataFrame, come mostrato qui:
    df_sales = df_sales[['Date','Empno','Total']]
    
    df_sales_emps = df_sales.merge(df_emps)
    df_result = df_sales_emps.merge(df_locations)
    print(df_result)
    
    df_result = df_result[['Date','Region','Total']]
    print(df_result)

    df_date_region = df_result.groupby(['Date','Region']).sum()
    print(df_date_region)
    
    print(df_date_region.index) # per vedere come lavora il multiindex
    
    #print(df_date_region[df_date_region.index.isin( [('2022-02-05', 'West')])])
    #print(df_date_region[df_date_region.index.isin([('2022-02-05', 'East'), ('2022-02-05', 'West')])])
    #print(df_date_region[df_date_region.index.isin([('2022-02-06', 'East'),('2022-02-04', 'East'), ('2022-02-05', 'West')])])
    
    # SLICING di aggregation
    print(df_date_region[('2022-02-04', 'East'):('2022-02-05', 'West')])
    
    print(df_date_region['2022-02-04':'2022-02-05'])
    
    print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice(None)), :])