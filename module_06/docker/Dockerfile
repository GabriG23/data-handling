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
