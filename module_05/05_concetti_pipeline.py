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
# versione 4 con google, funziona solo con lui
from deep_translator import GoogleTranslator
# versione 5 del modulo con Logistic Regression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# link: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
# link: https://textblob.readthedocs.io/en/dev/

def feedback_inviati(): # mi creo una lista di stringhe e creo il df
    print("Inizio acquisizione dei feedback degli utenti")
    feedbacks = [
        "Evento sulle AI grandioso!!",
        "evento un po' lunghetto",
        "mi sono divertito. grandi!!",
        "Complimenti, è stato interessante!&%",
        "pazzesco, non pensavo fosse così",
        "non è andata bene"
    ]
    feedbacks_inglese = [
        "very good",
        "that was boring",
        "that was incredible boring",
        "best event ever",
        "I found love in this event",
        "Amzing, never felt so happy"
    ]
    return pd.DataFrame({'Commento': feedbacks_inglese})

def pulizia_testo(df):  # concetti python: espressioni regolari
    # Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi all'inizio/fine dei commenti
    # Convertire tutti i commenti in minuscolo per garantire uniformità
    print("Pulizia del testo")
    def clean(testo):
        # espressioni regolari come nel modulo 4
        testo = re.sub(r'[^\w\s]', '', testo) # sostituisce la punteggiatura con '', quindi rimuovendolo
                                # prende solo le parole che hanno spazi e hanno caratteri letterari con \w
        testo = testo.strip().lower()   # strip rimuove gli spazi e lower mette tutto in minuscolo
        return testo
    df['Pulito'] = df['Commento'].apply(clean)
    return df

def estrazione_parole_chiave(df):   # concetti python: NLP
    # Estrarre le parole chiave principali da ciascun commento
    print("Estrazioni parole chiave")
    vectorizer = TfidfVectorizer(max_features=3)
    X = vectorizer.fit_transform(df['Pulito'])
    parole_chiave = vectorizer.get_feature_names_out()
    print(f"Parole chiave principali: {parole_chiave}")
    return parole_chiave

def analisi_del_sentiment_logistic_regression(df):  # preso dal modulo 5
    # non funziona in italiano, classificazione binaria, niente score ma solo 0 o 1
    print("Analisi del sentiment con modello di Machine Learning (Logistic Regression)")

    path = '../dataset/sentiment_labelled_sentences/amazon_cells_labelled.txt'
    df_sentiment = pd.read_csv(path, names=['review', 'sentiment'], sep='\t')

    reviews = df_sentiment['review'].values
    sentiments = df_sentiment['sentiment'].values
    reviews_train, reviews_test, sentiments_train, sentiments_test = train_test_split(
        reviews, sentiments, test_size=0.2, random_state=42
    )

    vectorizer = CountVectorizer()
    vectorizer.fit(reviews_train)
    x_train = vectorizer.transform(reviews_train)
    classifier = LogisticRegression()
    classifier.fit(x_train, sentiments_train)

    x_feedback = vectorizer.transform(df['Pulito'])
    predizioni = classifier.predict(x_feedback)
    df['Sentiment'] = predizioni  # 0 = negativo, 1 = positivo

    return df

def analisi_del_sentiment_text_blob(df):           # concetti python: sentiment
     # senza traduzione, ottengo sentiment uguali a 0
    # Determinare se il sentiment generale (positivo, negativo, neutro) di ciascun commento.
    print("Analisi del sentiment con text_blob")
    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity  # va da -1 a +1
    df['Sentiment'] = df['Pulito'].apply(get_sentiment)
    return df

def analisi_del_sentiment_google(df):
    # lento, funziona anche in italiano perchè traduco
    print("Analisi del sentiment con traduzione")
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

    feedback_df = analisi_del_sentiment_logistic_regression(feedback_df) # con classificatore addestrato, va male in italiano
    print(feedback_df[['Pulito', 'Sentiment']])
    print("\n" + "*"*30 + "\n")

    calcolo_sentiment_medio(feedback_df)
    print("\n" + "*"*30 + "\n")
    
    feedback_df = analisi_del_sentiment_text_blob(feedback_df)    # con text blob, non funziona in italiano
    print(feedback_df[['Pulito', 'Sentiment']])
    print("\n" + "*"*30 + "\n")

    calcolo_sentiment_medio(feedback_df)
    print("\n" + "*"*30 + "\n")
    
    feedback_df = analisi_del_sentiment_google(feedback_df)    # funziona con italiano perché traduco ma è lento
    print(feedback_df[['Pulito', 'Sentiment']])
    print("\n" + "*"*30 + "\n")

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
- .polarity: valore da -1 (negativo) e +1 (positivo)
- .subjectivity: valore tra 0.0 (oggettivo) e 1.0 (soggettivo)
textblob va bene per testi semplici e corti, come in questo esercizio.
Per testi più complessi meglio usare qualche altro modello

'''