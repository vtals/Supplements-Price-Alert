import pandas as pd
from datetime import datetime
from config import PROTEIN_URL, CREATINE_URL
from scraper import get_protein_data, get_creatine_data

today = datetime.now().strftime('%Y-%m-%d')


def update_protein_data():
    
    '''
    This function updates the protein dataset by appending new data to the existing CSV file.
    '''
    
    new_protein_data = get_protein_data(PROTEIN_URL)
    new_protein_df = pd.DataFrame(new_protein_data, columns=['flavour', 'weight_in_g', 'price', 'price_discounted', 'price_currency', 'date'])

    new_protein_df.to_csv('data/bulk_protein_data.csv', mode='a', header=False,  index=False)
    protein_df_updated = pd.read_csv('data/bulk_protein_data.csv')
    print("Protein data updated successfully.")

    return protein_df_updated



def update_creatine_data():
    
    '''
    This function updates the creatine dataset by appending new data to the existing CSV file.
    '''
    
    new_creatine_data = get_creatine_data(CREATINE_URL)
    new_creatine_df = pd.DataFrame(new_creatine_data, columns=['flavour', 'weight_in_g', 'price', 'price_discounted', 'price_currency', 'date'])
 
    new_creatine_df.to_csv('data/bulk_creatine_data.csv', mode='a', header=False, index=False)
    creatine_df_updated = pd.read_csv('data/bulk_creatine_data.csv')
    print("Creatine data updated successfully.")
    
    return creatine_df_updated

