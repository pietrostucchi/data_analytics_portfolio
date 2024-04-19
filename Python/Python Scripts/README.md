# Python Scripts

## Project Summary

In this repo, I'm showing some of my skills with Web Scraping, API and, in general, the development of some algorithms.

In particular, you can see two scripts in which I've used these libraries and modules:
* pathlib (Path)
* os
* bs4 (BeautifulSoup)
* datetime (datetime, date, timedelta)
* time
* pandas
* dateutil (relative.delta)
* seaborn

## Files 

```script_1```: it's about Bitcoin price in Euro in the last month (data provided by [CoinGecko](https://www.coingecko.com/))  
```script_2```: it's about products of ten of the makeup brands available in the [Makeup API](https://makeup-api.herokuapp.com/)

## Scripts in details

In ```script_1``` I start by creating a new folder, '1_unprocessed', to save in csv files obtained by API requests. Data retrieved in this way are daily statistics about Bitcoin.
Then, these files are moved from '1_unprocessed' to a new folder called '2-processed' . With every move, they are concatenated in a new dataframe and, in the end of the cycle, the starting folder is deleted.
This dataframe contains statistics data about Bitcoin for every day of last month.
Finally, I draw a time series for the exchange between Bitcoin and Euro and save it as png locally. 

#### Notes to ```script_1```: 

I've cared to generalize: 
1. path objects, so that this script can be run without problems by anyone
2. time limits of the last month, that are calculated based on the date the script is started

Also in ```script_2``` I start by creating a folder, 'mkp', to save in csv files. Before to retrieve data with API requests, I scrape the list of all brands available in the website and choose ten of them randomly. Then, the files are concatenated into a single dataframe to plot the amount of products per brand and save it as png file locally. Finally, 'mkp' folder and its files are deleted.

### Thanks for reading!