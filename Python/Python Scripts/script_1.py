#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%

# import the necessary libraries

import os
from pathlib import Path
from datetime import datetime, date, timedelta
import requests
import time
import pandas as pd
from dateutil.relativedelta import relativedelta
import seaborn as sns

# %%

# get the current working directory as 'cwd' variable and, if it doesn't exist yet, create the directory '1_unprocessed'

cwd = os.getcwd()
try:
    os.mkdir(cwd+'/1_unprocessed')
    print('1_unprocessed directory created')
except FileExistsError:
    print('1_unprocessed directory you are trying to create already exists')


#%%

# create a variable 'datafolder' to call it in the next steps    

datafolder = Path(__file__).parent / '1_unprocessed'


#%%

# create a list of days of the last month

last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
first_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
date_list = pd.date_range(first_day_of_prev_month, last_day_of_prev_month)\
    .strftime('%d-%m-%Y').to_list() # format dates as required by the API
print(f'Days to retrieve: {len(date_list)}')

#%%

# create get_csv() function to call it in the next steps

def get_csv(url):

    # send get request to specified url and print status code
    r = requests.get(url)
    print('Loading', str(day), '| status code', str(r.status_code))

    # create a dataframe and save it as csv file in the specified directory
    try: 
        tmp_df = pd.DataFrame.from_dict(r.json()['market_data']).reset_index()
        tmp_df['date'] = day
        tmp_df.to_csv(datafolder/('btc_' + day + '.csv'))
        time.sleep(8)
    except:
        print('Encountered an error, sleeping for 120 seconds')
        time.sleep(120)
        r = requests.get(url)
        print('Loading', str(day), '| status code', str(r.status_code))
        tmp_df = pd.DataFrame.from_dict(r.json()['market_data']).reset_index()
        tmp_df['date'] = day
        tmp_df.to_csv(datafolder/('btc_' + day + '.csv'))
     

#%%

# check if there are any files yet; 
# if no, make the requests for the json to save as csv; 
# if yes, check how many they are and, if they are less then the days of last month, complete the requests till the last; 
# otherwise, if there are already all the files, do nothing
tot_days = len(date_list)
last_month = datetime.now() - relativedelta(months=1)
m_text = format(last_month, '%B').lower()
m_Y = format(last_month, '%m %Y')
month_year = m_Y.replace(' ', '-')


#%%

if len(os.listdir(datafolder)) == 0:  
    for day in date_list:
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + day
        get_csv(url)
    print('Completed')

# different cases to retrieve correct date depending on the number of files already downloaded
elif len(os.listdir(datafolder)) < tot_days: 
    print(f'You are writing csv in a folder that already contains {len(os.listdir(datafolder))} files')
    while len(os.listdir(datafolder)) < tot_days:
        if len(os.listdir(datafolder)) < 9:        
            last_file = os.listdir(datafolder)[-1]
            day = f'0{int(last_file[4:6])+1}-{month_year}' # insert a 0 digit because of the conversion to int
            url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + day
            get_csv(url)
        else:
            last_file = os.listdir(datafolder)[-1]
            day = f'{int(last_file[4:6])+1}-{month_year}'
            url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + day
            get_csv(url)
    print(f'Now there are {len(os.listdir(datafolder))} files')

else:
    print(f'You already have {len(os.listdir(datafolder))} files. Check below:\n')
    for file in os.listdir(datafolder):
        print(file)


#%%

# create new directory 2_processed if it doesn't exist

new_folder = cwd+'/2_processed'

if os.path.exists(new_folder) == False: 
    os.mkdir(new_folder)
    print('Directory 2_processed created')
else:
    print('Directory 2_processed already exists')


#%%

# concatenate files in df dataframe and save each of them in the new directory 2_processed
# remove empty directory 1_unprocessed
# then, save new dataframe as btc_{m_text}.csv

files = os.listdir(datafolder)

if len(os.listdir(new_folder)) == 0:
    df = pd.DataFrame()
    for file in files:
        tmp_df = pd.read_csv(datafolder/file)
        df = pd.concat([df, tmp_df])
        os.rename(f'{datafolder}/{file}', f'{new_folder}/{file}')
    os.rmdir(datafolder)
    df.to_csv(Path(new_folder).parent/f'btc_{m_text}.csv')
else:
    print('You already did this job')


#%%  

# read btc_last_month.csv and check its info

btc_last_month = pd.read_csv(f'btc_{m_text}.csv')
btc_last_month.info()


#%%

# clean dataframe btc_last_month and show its first five lines

btc_last_month.index = pd.RangeIndex(len(btc_last_month))
btc_last_month['date'] = pd.to_datetime(btc_last_month['date'], format='%d-%m-%Y')
btc_last_month.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)
btc_last_month.rename(columns={'index': 'currency'}, inplace=True)
btc_last_month.head()


#%%

# create lineplot of Bitcoin price in Euro and save it

sns.set_theme(rc={'figure.figsize':(15, 8)})
final_plot = sns.lineplot(x='date', y='current_price', data=btc_last_month[btc_last_month['currency'] == 'eur'])
final_plot.get_figure().autofmt_xdate() 
final_plot.set(title=f'Bitcoin Price Chart (BTC/EUR) {m_text}', xlabel='', ylabel='Price in Euro')
final_plot.get_figure().savefig(cwd+(f'/btceur_line_plot_{m_text}.png'))

print(f'csv and png files about {m_text} saved correctly')