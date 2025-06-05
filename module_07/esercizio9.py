from pymongo import MongoClient

'''
Esercizio 9: Inserire e interrogare più documenti
Continuando con l’insieme emps creato nel database sampledb, provate a eseguire
inserti massivi con il metodo insert_many() e interrogate più di un documento con il metodo find()

link insert_many(): https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
link find(): https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find
'''

if __name__ == '__main__':
    client = MongoClient("mongodb://admin:secret@localhost:27017/")
    db = client['sampledb'] # per accedere agli attributi: db = client.sampledb
    emps_collection = db['emps']

    employees = [
        {"empno": 9002, "empname": "Alice Smith", "orders": [2609, 2618]},
        {"empno": 9003, "empname": "Bob Johnson", "orders": [2610]},
        {"empno": 9004, "empname": "Charlie Brown", "orders": [2611, 2621, 2630]}
    ]
    result_insert = emps_collection.insert_many(employees)
    print(f"Documenti inseriti, id: {result_insert.inserted_ids}")

    print("Documenti trovati:")
    for emp in emps_collection.find():
        print(emp)