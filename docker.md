# Docker
- installare Docker da: {link}[https://www.docker.com/products/docker-desktop/], selezionare windows AMD64
- verificare l'installazione con `docker --version`
- creare una cartella `docker`
- creare un `Dockerfile` senza estenzione, scrivere dentro (questo è un esempio con Python 3.11):
```
# Usa l'immagine base ufficiale di Python 3.11
FROM python:3.11-slim

# Imposta la directory di lavoro dentro al container
WORKDIR /app

# Copia i file locali nella directory di lavoro del container
COPY . .

# Installa le dipendenze (se hai un requirements.txt)
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Comando di default (modificabile)
CMD ["python"]
```

- aggiungere un requirements.txt con le librerie:
```
pandas
numpy
matplotlib
seaborn
```

- costruisci il container: in questo caso `docker build -t python-app:3.11 .`
- per avviare una sessione interattiva `docker run -it --rm python-app:3.11`
- per aprire il bash: `docker run -it --rm -v ${PWD}:/app python:3.11 bash`
- cambiare cartella `cd app`
- eseguire il file python con `python main.py`

# Redis

- usare da docker `docker run --name redis-stack -d -p 6379:6379 redis/redis-stack-server:latest`
- per visualizzare i container attivi docker ps
- per mandare un ping: docker exec -it redis-stack redis-cli ping


# MongoDB
- docker pull mongodb/mongodb-community-server:latest
- Installare un container docker `docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret -v mongodata:/data/db mongo`