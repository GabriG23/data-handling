'''
Esercizio 5: Concetti di pipeline per l'analisi di feedback testuali
Considera di dover analizzare un set di feedback testuali inviati ai partecipanti a un evento (ad esempio, un file di testo semplice o un elenco di commenti).
Identifica e descrivi brevemente quali passaggi della pipeline di elaborazione dati (Acquisizione, Pulizia, Trasformazione, Analisi, Immagazzinamento) sarebbero necessari per:
    - Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi all'inizio/fine dei commenti
    - Convertire tutti i commenti in minuscolo per garantire uniformità
    - Estrarre le parole chiave principali da ciascun commento
    - Determinare se il sentiment generale (positivo, negativo, neutro) di ciascun commento.
    - Calcolare il sentimenti medio complessivo per tutti i feedback
    - Salvare i risultati dell'analisi (sentiment per commento, sentimento medio) in un formato strutturato.
Per ogni passaggio, menziona brevemente quali librerie o tecniche Python viste (anche concettualmente, come
l'elaborazione del linguaggio naturale - NLP42 o l'analisi del sentiment44) potrebbero essere utili
'''

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Analisi del sentiment
from textblob import TextBlob       # versione 1

# installare questo per la traduzione     # versione 2
# pip install textblob googletrans==4.0.0-rc1
# non funziona
import nltk                         # versione 3 come da modulo
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
# versione 4con google, funziona solo con lui
from deep_translator import GoogleTranslator
from nltk.sentiment import SentimentIntensityAnalyzer


# link: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
# link: https://textblob.readthedocs.io/en/dev/

def feedback_inviati():
    print("Inizio acquisizione dei feedback degli utenti")
    # feedbacks = [
    #     "Evento sulle Ai SUPER!!",
    #     "evento un po' lunghetto",
    #     "mi sono divertito. grandi!!",
    #     "Complimenti, è stato interessante!&%",
    #     "pazzesco, non pensavo fosse così",
    #     "non è andata bene"
    # ]

    feedbacks_inglese = [
        "very good",
        "that was boring",
        "that was incredible boring",
        "best event ever",
        "I found love in this event",
        "Amzing, never felt so happy"
    ]

    feedbacks = [
        " Bellissimo evento!!! 👍👏 ",
        "Troppo lungo, mi sono annoiato...",
        "Molto ben organizzato. Complimenti!",
        "non mi è piaciuto per niente",
        "Ottima esperienza, staff gentile.",
        "   Meh.  "
    ]
    return pd.DataFrame({'Commento': feedbacks_inglese})

def pulizia_testo(df):
    # Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi all'inizio/fine dei commenti
    # Convertire tutti i commenti in minuscolo per garantire uniformità
    print("Pulizia del testo")
    def clean(testo):
        # espressioni regolari come nel modulo 4
        testo = re.sub(r'[^\w\s]', '', testo) # sostituisce la punteggiatura con '', quindi rimuovendolo
        testo = testo.strip().lower()   # strip rimuove gli spazi e lower mette tutto in minuscolo
        return testo
    df['Pulito'] = df['Commento'].apply(clean)
    return df

def estrazione_parole_chiave(df):
    # Estrarre le parole chiave principali da ciascun commento
    print("Estrazioni parole chiave")
    vectorizer = TfidfVectorizer(max_features=3)
    X = vectorizer.fit_transform(df['Pulito'])
    parole_chiave = vectorizer.get_feature_names_out()
    print(f"Parole chiave principali: {parole_chiave}")
    return parole_chiave

def analisi_del_sentiment_1(df):            # senza traduzione, ottengo sentiment uguali a 0
    # Determinare se il sentiment generale (positivo, negativo, neutro) di ciascun commento.
    print("Analisi del sentiment")
    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity  # va da -1 a +1
    df['Sentiment'] = df['Pulito'].apply(get_sentiment)
    return df

def analisi_del_sentiment_2(df):
    print("Analisi del sentiment")
    def get_sentiment(text):
        try:
            tradotto = TextBlob(text).translate(to='en')
            return tradotto.sentiment.polarity
        except Exception as e:
            print(f"Errore nella traduzione: {e}")
            return 0  # fallback
    df['Sentiment'] = df['Pulito'].apply(get_sentiment)
    return df


def analisi_del_sentiment_3(df):
    print("Analisi del sentiment con VADER (inglese)")

    sia = SentimentIntensityAnalyzer()

    def get_sentiment(text):
        try:
            tradotto = TextBlob(text).translate(to='en')
            score = sia.polarity_scores(str(tradotto))  # ottieni un dizionario con pos, neu, neg, compound
            return score['compound']  # il valore 'compound' riassume tutto: da -1 (negativo) a +1 (positivo)
        except Exception as e:
            print(f"Errore nella traduzione/sentiment: {e}")
            return 0

    df['Sentiment'] = df['Pulito'].apply(get_sentiment)
    return df


def analisi_del_sentiment_4(df):
    print("Analisi del sentiment con traduzione + VADER")
    sia = SentimentIntensityAnalyzer()

    def get_sentiment(text):
        try:
            tradotto = GoogleTranslator(source='auto', target='en').translate(text)
            score = sia.polarity_scores(tradotto)
            return score['compound']
        except Exception as e:
            print(f"Errore nella traduzione/sentiment: {e}")
            return 0

    df['Sentiment'] = df['Pulito'].apply(get_sentiment)
    return df

def calcolo_sentiment_medio(df):
    # Calcolare il sentimenti medio complessivo per tutti i feedback
    media = df['Sentiment'].mean()
    print(f"Sentiment medio complessivo: {round(media, 2)}")
    return media

def salvataggio_risultati(df):
    # Salvare i risultati dell'analisi (sentiment per commento, sentimento medio) in un formato strutturato.
    print("Salvataggio su file")
    df.to_csv("risultati_feedback_es05_module_05.csv", index=False)
    print("I risultati sono stati salvati in 'risultati_feedback_es05_module_05.csv'")

if __name__ == '__main__':
    feedback_df = feedback_inviati()
    print("\n" + "*"*30 + "\n")

    feedback_df = pulizia_testo(feedback_df)
    print(feedback_df[['Commento', 'Pulito']])
    print("\n" + "*"*30 + "\n")

    estrazione_parole_chiave(feedback_df)
    print("\n" + "*"*30 + "\n")

    feedback_df = analisi_del_sentiment_1(feedback_df)
    print(feedback_df[['Pulito', 'Sentiment']])
    print("\n" + "*"*30 + "\n")

    # feedback_df = analisi_del_sentiment_2(feedback_df)
    # print(feedback_df[['Pulito', 'Sentiment']])
    # print("\n" + "*"*30 + "\n")

    # feedback_df_2 = analisi_del_sentiment_3(feedback_df)
    # print(feedback_df[['Pulito', 'Sentiment']])
    # print("\n" + "*"*30 + "\n")

    # feedback_df_3 = analisi_del_sentiment_4(feedback_df)
    # print(feedback_df[['Pulito', 'Sentiment']])
    # print("\n" + "*"*30 + "\n")

    calcolo_sentiment_medio(feedback_df)
    print("\n" + "*"*30 + "\n")

    salvataggio_risultati(feedback_df)


'''
TfidfVectorizer
è una classe di scikit-learn usata per trasformare del testo in numeri, in modo che possa essere usato da modelli di ML.
TF-IDF sta per
- TF = Term Frequency --> frequenza del termine
- IDF = Inverse Document Frequency --> frequenza inversa nei documenti
quindi per esempio
- TF conta quante volte appaiono le parole in un documento
- IDF ti dice quanto è rara una parola nei documenti 
    IDF(term) = log(N / (1 + n_t))
    dove N è il numero totale di documenti
    n_t = numero di documenti che contengono quel termine
- infine moltiplica i due punteggi per lo score finale TF * IDF


TextBlob
è una libreria Python per elaborare testi NLP, utile per l'analisi del sentiment per esempio
Analisi del sentiment
- è un metodo per determinare il tono emozionale di un testo, quindi positivo, negativo, neutro
la libreria lo fa in automatico restituiendo due valori
- polarity: valore da -1 (negativo) e +1 (positivo)
- .subjectivity: valore tra 0.0 (oggettivo) e 1.0 (soggettivo)
textblob va bene per testi semplici e corti, come in questo esercizio.
Per testi più complessi meglio usare qualche altro modello

'''