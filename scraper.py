import json, requests
from bs4 import BeautifulSoup
import pandas as pd
from config import HEADERS, PROTEIN_URL, CREATINE_URL
from datetime import datetime


def get_protein_data(url=PROTEIN_URL):
    
    '''
    This function scrapes protein data from the given URL and returns a list of tuples containing the data.
    '''
    
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        response = requests.get(url, headers=HEADERS, timeout=10) 
        soup = BeautifulSoup(response.content, 'html.parser')
        l = []
        data = json.loads(soup.find('script', type='application/ld+json').string)
        offers = data.get('offers')
        for offer in offers:
            price = offer.get('priceSpecification').get('price')
            price_discounted = offer.get('price')    
            price_currency = offer.get('priceCurrency') 
            sku = offer.get('sku').split('-')
            flavour = sku[2]
            weight = sku[-1]      
            l.append((flavour, weight, price, price_discounted, price_currency, today))  
        
        return l
        

    except requests.exceptions.RequestException as e:
        print(f"Error fetching protein data: {e}")
        return []


def create_protein_df():
    
    '''
    This function creates a DataFrame for protein data and saves it to a CSV file.  
    '''

    protein_df = pd.DataFrame(get_protein_data(), columns=['flavour', 'weight_in_g', 'price', 'price_discounted', 'price_currency', 'date'])
    protein_df.to_csv('data/bulk_protein_data.csv', index=False)
    return protein_df
    

def get_creatine_data(url=CREATINE_URL):
    
    '''
    This function scrapes protein data from the given URL and returns a list of tuples containing the data.
    '''
    
    today = datetime.now().strftime('%Y-%m-%d')
    try:
        response = requests.get(url, headers=HEADERS, timeout=10) 
        soup = BeautifulSoup(response.content, 'html.parser')
        l = []
        data = json.loads(soup.find('script', type='application/ld+json').string)
        offers = data.get('offers')
        for offer in offers:
            price = offer.get('priceSpecification').get('price')
            price_discounted = offer.get('price')    
            price_currency = offer.get('priceCurrency') 
            sku = offer.get('sku').split('-')
            flavour = sku[2]
            weight = sku[3]      
            l.append((flavour, weight, price, price_discounted, price_currency, today))
    
        return l
        

    except requests.exceptions.RequestException as e:
        print(f"Error fetching creatine data: {e}")
        return []
    

def create_creatine_df():
        
    '''
    This function creates a DataFrame for creatine data and saves it to a CSV file.  
    '''
    creatine_df = pd.DataFrame(get_creatine_data(), columns=['flavour', 'weight_in_g', 'price', 'price_discounted', 'price_currency', 'date'])
    creatine_df.to_csv('data/bulk_creatine_data.csv', index=False)
    return creatine_df

