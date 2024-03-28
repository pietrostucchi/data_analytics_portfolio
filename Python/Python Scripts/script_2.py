#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%

# to import necessary libraries

import numpy as np
import pandas as pd
import os
from pathlib import Path
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup


#%%

# to create mkp directory in data folder if it doesn't exist yet

folder = Path(__file__).parent / 'mkp'

try:
    os.mkdir(folder)
    print('mkp directory created')
except FileExistsError:
    print('mkp directory already exists') 


#%%
    
# to scrape list of all brands available in the Makeup API with BeautifulSoup library

url = 'https://makeup-api.herokuapp.com/'
page = requests.get(url)
print('makeup-api request status code:', page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='tag_list')
brands = results[1]
brand_list = brands.find_all('div', class_='tag')


#%%

# to create list of all brands and randomly choose 10 of all available brands

mkp_brands = []
for brand in brand_list:
    mkp_brands.append(brand.find('h4').text)

mkp_brands_10 = np.random.choice(mkp_brands, size=10, replace=False)
mkp_brands_10


#%%

# to retrieve json data about each brand (among those just chosen) and save them as csv files in mkp directory created above

for brand in mkp_brands_10:
    url = 'https://makeup-api.herokuapp.com/api/v1/products.json?brand='+brand
    r = requests.get(url)
    print(brand, '| status code:', r.status_code)
    mkp_tmp = pd.DataFrame.from_dict(r.json())
    mkp_tmp.to_csv(folder/(brand+'.csv'))


#%%
    
# to retrieve list of all the files just saved in mkp directory

files = os.listdir(folder)
files


#%%

# to loop through all the files and create a dataframe which includes all of them

df = pd.DataFrame()
mkp_tmp = pd.DataFrame()
for brand in files:
    mkp_tmp = pd.read_csv(folder/brand, index_col=0)
    df = pd.concat([df, mkp_tmp])


#%%
    
# to reset index and check info of dataframe just created

df.reset_index(inplace=True, drop=True)
df.info()


#%%

df.head()


# %%

df = df.drop(['id'], axis=1)


#%%

# to create a barplot showing the number of products available for each brand

prod_each_brand = pd.DataFrame(df['brand'].value_counts())
prod_each_brand.reset_index(inplace=True)

sns.set_theme(rc={'figure.figsize':(15, 8)})
plot = sns.barplot(x='count', y='brand', data=prod_each_brand)
plot.set(title='Amount of Products per Brand',
         xlabel='Amount',
         ylabel='Brand')
plt.show()


# %%

# to save a copy of the plot locally

plot.get_figure().savefig('tot_products_per_brand.png')


#%%

# to remove files from mkp folder and, then, the folder itself

for file in os.listdir(folder):
    os.remove(folder/file)

os.rmdir(folder)

print('Completed!')
