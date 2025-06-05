import mysql.connector
'''
Esercizio #8: Eseguire una join uno-a-molti
Modificate il codice mostrato nella sezione precedente in modo che la query sia una join
della tabella emps con la tabella orders. È possibile mantenere la condizione che empno sia
maggiore di 9001. Adattate la chiamata print() per produrre le righe della join modificata.
'''
def connection():

    try:  
        cnx = mysql.connector.connect(user='root', password='PASSWORD_DI_GABRI',
                                    host='127.0.0.1',
                                    database='sampledb')
        cursor = cnx.cursor()
        query = ("""SELECT e.empno, e.empname, e.job, o.total FROM emps AS e JOIN orders AS o ON e.empno = o.empno WHERE e.empno > %s""")
        empno = 9001
        cursor.execute(query, (empno,))
        for (empno, empname, job, total) in cursor:
            print("{}, {}, {}, {}".format(empno, empname, job, total))
    except mysql.connector.Error as err:
        print("Error-Code:", err.errno)
        print("Error-Message: {}".format(err.msg))
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    connection()
 