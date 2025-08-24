import schedule
import time
from datetime import datetime
from updater import update_protein_data, update_creatine_data
from alert_bot import telegram_bot_sendtext, check_price_alert
from scraper import create_creatine_df, create_protein_df
import os




def main():
    
    '''
    This is the main function that checks for existing data files, creates or updates datasets, then checks for price alerts and sends a summary message via Telegram.
    '''
    
    if not os.path.exists('data/bulk_protein_data.csv') and not os.path.exists('data/bulk_creatine_data.csv'):
        print("No data files found. Creating initial datasets.")
        protein_df = create_protein_df()
        creatine_df = create_creatine_df()
    else:
        print("Data files found. Proceeding with updates.")
        protein_df = update_protein_data()
        creatine_df = update_creatine_data()
        print("Checking for price alerts...")
        check_price_alert(protein_df, 'Protein')
        check_price_alert(creatine_df, 'Creatine')
    
    telegram_bot_sendtext(f"Dataset aggiornati con successo il {datetime.now().strftime('%Y-%m-%d')}")
    print("Weekly check completed.")
    return protein_df, creatine_df


'''
Schedule the weekly update to run every Monday at midnight

schedule.every().monday.at("00:00").do(weekly_update, TEXT)

while True:
    schedule.run_pending()
    time.sleep(5)
    
'''

if __name__ == "__main__":
    main()
    print("Script just executed.")
