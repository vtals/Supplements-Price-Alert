import pandas as pd
from datetime import datetime
from config import PROTEIN_URL, CREATINE_URL

def update_protein_data(get_protein_data):
    protein_df = pd.read_csv('data/bulk_protein_data.csv')

    new_protein_data = get_protein_data(url=PROTEIN_URL)
    protein_df_new = pd.DataFrame(new_protein_data, columns=['flavour', 'weight in g', 'price', 'price_discounted', 'price_currency'])
    protein_df_new['date'] = datetime.now().strftime('%Y-%m-%d')
    
    protein_df_updated = pd.concat([protein_df, protein_df_new], ignore_index=True)
    protein_df_updated.to_csv('data/bulk_protein_data.csv', index=False)
    
    return protein_df_updated



def update_creatine_data(get_creatine_data):
    creatine_df = pd.read_csv('bulk_creatine_data.csv')

    new_creatine_data = get_creatine_data(url=CREATINE_URL)
    creatine_df_new = pd.DataFrame(new_creatine_data, columns=['flavour', 'weight in g', 'price', 'price_discounted', 'price_currency'])
    creatine_df_new['date'] = datetime.now().strftime('%Y-%m-%d')
    
    creatine_df_updated = pd.concat([creatine_df, creatine_df_new], ignore_index=True)
    creatine_df_updated.to_csv('data/bulk_creatine_data.csv', index=False)
    

    return creatine_df_updated
