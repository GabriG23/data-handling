# Esercizio : Filtrare i dati con una comprensione di lista
# Nella sezione precedente, è stata filtrata la lista orders per ottenere solo una lista di taxi
# non disponibili, convertendo prima orders in un DataFrame. Si provi ora a generare la lista
# unavailable_list senza pandas, utilizzando invece una comprensione di lista. Con questo
# approccio, è possibile ottenere la lista dei taxi assegnati agli ordini attualmente aperti con
# una sola riga di codice:
# unavailable_list = [x[2] for x in orders if x[1] == "open"]
# Dopo questa sostituzione, non sarà necessario modificare nient’altro nel resto dello script.

def unavailable():
    orders = [('order_039', 'open', 'cab_14'),
              ('order_034', 'open', 'cab_79'),
              ('order_032', 'open', 'cab_104'),
              ('order_026', 'closed', 'cab_79'),
              ('order_021', 'open', 'cab_45'),
              ('order_018', 'closed', 'cab_26'),
              ('order_008', 'closed', 'cab_112'),]

    # lista dei taxi non disponibili
    unavailable_list = [x[2] for x in orders if x[1] == "open"]
    print(unavailable_list)

if __name__ == '__main__':
    unavailable()