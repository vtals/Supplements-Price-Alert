import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from config import BOT_TOKEN, CHAT_ID, PRICE_THRESHOLD




def telegram_bot_sendtext(text):
    '''
    This function connects to the Telegram Bot API and sends a message.
    '''

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
    }

    try:
        r = requests.post(url, data=payload)
        r.raise_for_status()
        print("Message sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")


def check_price_alert(df, supplement):
    
    '''
    This function checks for price errors in the dataframe and sends alerts via Telegram.
    '''

    today = datetime.now().strftime('%Y-%m-%d')

    new_items = df[df['date'] == today]
    new_items = new_items.copy()
    new_items['price_discounted'] = new_items['price_discounted'].astype(float)
    if new_items.empty:
        print(f"Nessun nuovo dato trovato per {supplement} oggi.")
    else:
        cheap_items = new_items[new_items['price_discounted'] < PRICE_THRESHOLD[supplement]]
        if cheap_items.shape[0]:
            text = f"Errore di prezzo per {supplement}:\n"
            for _, row in cheap_items.iterrows():
                text += f"Gusto {row['flavour']}\n Peso: {row['weight_in_g']}g\n Prezzo: {row['price_discounted']} {row['price_currency']}\n"
            telegram_bot_sendtext(text)
        else:
            telegram_bot_sendtext(f"Nessun errore di prezzo trovato per {supplement} oggi.\nCi sentiamo alla prossima!")
