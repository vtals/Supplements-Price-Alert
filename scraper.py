import json, requests
from bs4 import BeautifulSoup
import pandas as pd
from config import HEADERS, PROTEIN_URL, CREATINE_URL

def get_protein_data(url=PROTEIN_URL):
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
            l.append((flavour, weight, price, price_discounted, price_currency))  

        return l


    except requests.exceptions.RequestException as e:
        print(f"Error fetching protein data: {e}")
        return []
    
    
protein_df = pd.DataFrame(get_protein_data(PROTEIN_URL), columns=['flavour', 'weight in g', 'price', 'price_discounted', 'price_currency'])
protein_df['date'] = "2025-08-17" #project start date

protein_df.to_csv('data/bulk_protein_data.csv', index=False)

    

def get_creatine_data(url=CREATINE_URL):
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
            l.append((flavour, weight, price, price_discounted, price_currency))
        
        return l

    except requests.exceptions.RequestException as e:
        print(f"Error fetching creatine data: {e}")
        return []


creatine_df = pd.DataFrame(get_creatine_data(CREATINE_URL), columns=['flavour', 'weight in g', 'price', 'price_discounted', 'price_currency'])
creatine_df['date'] = "2025-08-17" #project start date

creatine_df.to_csv('data/bulk_creatine_data.csv', index=False)
