
'''
Esercizio 11: Aggiungere righe/colonne nuove a un array Numpy. Continuando con l'esempio precedente,
create un nuovo array NumPy a due colonne con le informazioni sullo stipendio di altri due mesi per ciascun dipendente.
Quindi, concatenate l'array esistente base_salary con l'array appena creato. Allo stesso modo, aggiungete una
nuova riga all'array base_salary, aggiungendo così le informazioni sullo stipendio di un altro dipendente.
Notate che quando si aggiunge una singola riga o colonna a un array NumPy, è
possibile utilizzare la funzione numpy.append() piuttosto che numpy.concatenate().
'''
import numpy as np

def load_data():
    jeff_salary = [2700, 3000, 3000]
    nick_salary = [2600, 2800, 2800]
    tom_salary = [2300, 2500, 2500]
    base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])

    maya_salary = [2200, 2400, 2400]
    john_salary = [2500, 2700, 2700]
    base_salary2 = np.array([maya_salary, john_salary])
    base_salary = np.concatenate((base_salary1, base_salary2), axis=0)

    new_month_salary = np.array([[3000],[2900],[2500],[2500],[2700]])
    base_salary = np.concatenate((base_salary, new_month_salary), axis=1)

    return base_salary

def add_row(base_salary):
    new_salary = np.array([[2400, 2600, 2600, 2700]])
    update_salary = np.append(base_salary, new_salary, axis=0)
    return update_salary

if __name__ == '__main__':
    print("Caricamento dei dati\n")
    base_salary = load_data()
    print(base_salary)
    
    base_salary = add_row(base_salary)
    print(f"Stampa con l'aggiunta di un dipendente\n {base_salary}")