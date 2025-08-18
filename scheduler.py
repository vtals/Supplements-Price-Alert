import schedule
import time
from config import PRICE_TRESHOLD
from scraper import get_protein_data, get_creatine_data
from updater import update_protein_data, update_creatine_data
from alert_bot import telegram_bot_sendtext, check_price_alert, TEXT




def weekly_update():

    protein_df = update_protein_data(get_protein_data)
    creatine_df = update_creatine_data(get_creatine_data)
    
    telegram_bot_sendtext(TEXT)
    
    check_price_alert(protein_df, 'Proteine', PRICE_TRESHOLD['protein'])
    check_price_alert(creatine_df, 'Creatina', PRICE_TRESHOLD['creatine'])
    print("Weekly update completed.")
    return protein_df, creatine_df



schedule.every().monday.at("00:00").do(weekly_update, TEXT)

while True:
    schedule.run_pending()
    time.sleep(5)