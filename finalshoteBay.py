from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re

source = requests.get('https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_pgn=1').text    
soup = BeautifulSoup(source, 'lxml')
items = soup.find('li', class_='s-item')

n=0

for items in soup.find_all('li', class_='s-item'):
    
    try:  
        item_title = items.find('h3', class_='s-item__title').text
    except Exception as e:
        item_title = 'None'
    
    print(item_title)
    
    try:  
        item_desc = items.find('div', class_='s-item__subtitle').text
    except Exception as e:
        item_desc = 'None'
    
    print(item_desc)
    
    try:
        item_brand = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes1').text.split(' ')[1]
    except Exception as e:
        item_brand = 'None'
    
    print(item_brand)
    
    try:
        item_model = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes2').text.split(' ')[1:]
        item_model = ' '.join(item_model)
    except Exception as e:
        item_model = 'None'
    
    print(item_model)
    
    try:
        item_features = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes3').text.split(' ')[1]
    except Exception as e:
        item_features = 'None'
    
    print(item_features)  
    
    try:  
        item_origin = items.find('span', class_='s-item__location s-item__itemLocation').text
        item_origin = re.sub('From ', '', item_origin)
    except Exception as e:
        item_origin = 'None'
    
    print(item_origin)
    
    try:
        item_price = items.find('span', class_='s-item__price').text
    except Exception as e:
        item_price = 'None'
    
    print(item_price)
    
    try:
        item_shipping = items.find('span', class_='s-item__shipping s-item__logisticsCost').text
    except Exception as e:
        item_shipping = 'None'
    
    print(item_shipping)
    
    try:
        item_top_seller = items.find('span', class_='s-item__etrs-text').text
    except Exception as e:
        item_top_seller = 'None'
    
    print(item_top_seller)
    
    try:
        item_stars = items.find('span', class_='clipped').text.split(' ')[0]
    except Exception as e:
        item_stars = 'None'
    
    print(item_stars)
    
    try:
        item_nreviews = items.find('a', class_='s-item__reviews-count').text.split(' ')[0]
    except Exception as e:
        item_nreviews = 'None' 
    
    print(item_nreviews)
    
    try:
        item_qty_sold = items.find('span', class_='s-item__hotness s-item__itemHotness').text.split(' ')
        if item_qty_sold[1] == 'sold':
            item_qty_sold = item_qty_sold[0]
        else:
            item_qty_sold = 0
    except Exception as e:
        item_qty_sold = 'None' 
        
    try:
        item_link = items.find('a', class_='s-item__link')['href']
    except Exception as e:
        item_link = 'None'
    
    print(item_link)
    print()

    df = pd.DataFrame(columns = ['Title', 'description',
                                     'Brand', 'Model', 'Features', 'Origin', 
                                     'Price', 'Shipping',
                                     'Top Seller','Stars', 'No. Of Reviews',
                                     'Qty Sold',  'Link'])
    
    
        
    df.loc[n, 'Title'] = item_title
    df.loc[n, 'description'] = item_desc
    df.loc[n, 'Brand'] = item_brand
    df.loc[n, 'Model'] = item_model
    df.loc[n, 'Features'] = item_features
    df.loc[n, 'Origin'] = item_origin
    df.loc[n, 'Price'] = item_price
    df.loc[n, 'Shipping'] = item_shipping
    df.loc[n, 'Top Seller'] = item_top_seller
    df.loc[n, 'Stars'] = item_stars
    df.loc[n, 'No. Of Reviews'] = item_nreviews
    df.loc[n, 'Qty Sold'] = item_qty_sold
    df.loc[n, 'Link'] = item_link    
    
    n+=1

df.head()
