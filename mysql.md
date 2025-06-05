# MySql

- installazione dal sito community (link)[https://www.mysql.com/products/community/]
- per cambiare password: `mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_pswd';`
- `mysql -uroot -p`
- `SHOW DATABASES`: mostra i database
- `CREATE DATABASE sampledb` crea una tabella
- `USE sampledb;` cambia la tabella in uso
- Per creare una tabella
```
CREATE TABLE emps (
    empno INT NOT NULL,
    empname VARCHAR(50),
    job VARCHAR(30),
    PRIMARY KEY (empno)
    );
```
CREATE TABLE salary (
    empno INT NOT NULL,
    salary INT,
    PRIMARY KEY (empno)
    );
Query
- `ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);` crea la relazione tra le tabelle
```
SELECT * FROM orders WHERE status = 'Shipped'; // ha un una info in più sullo stato
SELECT * FROM orders; // recuperare tutte le righe della tabella
SELECT pono, date FROM orders; // recupera solo alcune colonne
```
```
SELECT date, ticker, price, LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS prev_price
FROM stocks;

SELECT s.* FROM stocks AS s LEFT JOIN(
    SELECT DISTINCT(ticker) FROM(
        SELECT price/LAG(price) OVER(PARTITION BY ticker ORDER BY date) AS dif, ticker FROM stocks) AS b
        WHERE dif <0.99
    ) AS a
    ON a.ticker = s.ticker
    WHERE a.ticker IS NULL;
```