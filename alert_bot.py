import requests
from datetime import datetime
from config import BOT_TOKEN, CHAT_ID, PRICE_TRESHOLD

TEXT = f"Dataset aggiornati con successo il {datetime.now().strftime('%Y-%m-%d')}"


def telegram_bot_sendtext(text=TEXT):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
    }

    try:
        requests.post(url, data=payload)
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")


def check_price_alert(df, supplement, treshold=PRICE_TRESHOLD):

    today = datetime.now().strftime('%Y-%m-%d')

    new_items = df[df['date'] == today]
    if new_items.empty:
        print(f"Nessun nuovo dato trovato per {supplement} oggi.")
    else:
        cheap_items = new_items[new_items['price_discounted'] < treshold]
        if not cheap_items.empty:
            message = f"Errore di prezzo per {supplement}:\n"
            for _, row in cheap_items.iterrows():
                message += f"Gusto {row['flavour']}\n Peso: {row['weight in g']}g\n Prezzo: {row['price_discounted']} {row['price_currency']}\n"
            telegram_bot_sendtext(message)
        else:
            telegram_bot_sendtext(f"Nessun errore di prezzo trovato per {supplement} questa settimana.\nCi sentiamo alla prossima!")