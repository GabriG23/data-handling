# Esercizio : Aggiungere altre metriche per analizzare le dipendenze
# Continuando con il DataFrame della sezione precedente, si può notare che, sebbene sia
# probabile un collegamento tra le colonne priceRise e volumeRise, non è del tutto chiaro.
# Ad esempio, il 2022-12-16 il prezzo è sceso di circa il 5% e il volume delle vendite è aumentato
# del 10%, ma quasi lo stesso calo di prezzo del 2022-01-05 è stato accompagnato
# da un calo del 22% del volume delle vendite.

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def dataset():
    ticker = 'TSLA'     # prendo i dati da yahoo finance
    tkr = yf.Ticker(ticker)
    df = tkr.history(period='1mo')
    df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})

    df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))    # calcolo variazioni logaritmiche
    df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))

    # calcolo volume cumulato su 2 giorni precedenti e volume successivo
    df['volumeSum'] = df['Volume'].shift(1).rolling(2).sum().fillna(0).astype(int)
    df['nextVolume'] = df['Volume'].shift(-1).fillna(0).astype(int)
    return df, ticker

def statistics_outputs(df):
    # calcolo metriche aggiuntive
    significant_price_move = df[abs(df['priceRise']) > 0.05]     # Filtra giorni con forte variazione di prezzo
    correlation = df[['priceRise', 'volumeRise']].corr().iloc[0, 1]
    std_price = df['priceRise'].std()
    std_volume = df['volumeRise'].std()

    print("\nDati con priceRise e volumeRise:\n", df)
    print("\nGiorni con variazione di prezzo > ±5%:\n", significant_price_move)
    print("\nMedia volumeRise su tutti i giorni:", df['volumeRise'].mean().round(4))
    print("Media volumeRise nei giorni con priceRise > ±5%:", significant_price_move['volumeRise'].mean().round(4))
    print("Correlazione priceRise vs volumeRise:", round(correlation, 4))
    print("Deviazione std priceRise:", round(std_price, 4))
    print("Deviazione std volumeRise:", round(std_volume, 4))

def plot_analysis(df, ticker):
    plt.figure(figsize=(8, 5))  # scatter plot per esplorare la correlazione
    plt.scatter(df['priceRise'], df['volumeRise'], c='blue', alpha=0.6)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.title(f'Relazione tra Variazioni Prezzo e Volume - {ticker}')
    plt.xlabel('Variazione logaritmica del prezzo (priceRise)')
    plt.ylabel('Variazione logaritmica del volume (volumeRise)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df, ticker = dataset()
    statistics_outputs(df)
    plot_analysis(df, ticker)
