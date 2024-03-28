# Jupyter Notebooks

## Summary

Here, I would like to show some code made with three Jupyter Notebooks.  
I used these libraries to retrieve, clean, manipulate and plot some insights:
* pandas
* numpy
* os
* requests
* matplotlib
* seaborn

The databases are from Kaggle, where you can find the entires datasets, and from Seaborn library.  
Link to databases on Kaggle: [Software Industry Salary Dataset - 2022](https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022?search=salary) and [Indian Startups - Funding Data](https://www.kaggle.com/datasets/omkargowda/indian-startups-funding-data?select=startup_funding2019.csv).

In the first notebook, software_professional_salaries, I explored Software_Professional_Salaries.csv.  
In the second, the startup_funding csv files of 2019, 2020 and 2021.  
All of these csv files are in data folder.  
In the third notebook, diamonds_taxis, I precisely worked on diamonds and taxis datasets directly loaded from Seaborn.

## Files

```data```: csv data folder  
```software_professional_salaries```: Jupyter Notebook for exploratory analysis  
```startup_funding```: Jupyter Notebook for exploratory analysis  
```diamonds_taxis```: Jupyter Notebook for exploratory analysis

## Informations to retrieve

In ```software_professional_salaries``` notebook, I looked for these info:
* how many unique Job Roles are in the dataset?
* how many unique Job Title for 'Python' Job Role?
* how many Company Name with 'Python' Job Role and Job Title containing substring 'Analyst'?
* which is the Company Name with highest number of Salaries Reported?
* how many Locations is this company present in?
* convert Salary from Indian Rupees to EUR (rounded to zero decimals) in new column Salary EUR 
* what's the Salary EUR on average for 'Python' Job Role?
* which is the Company Name with the highest average Salary EUR across all Job Titles?
* scatterplot of the relationship between the average Salary EUR and the average Rating for each Company
* which Company is causing the oddity in the scatterplot?
    
(currency conversion rates by [Exchange Rate API](https://www.exchangerate-api.com))
  
In ```startup_funding``` notebook, I answered these questions:
* what is the total 'Amount($)' of funding given in the three years available?
* which 'Investor' funded the highest number of 'Company/Brand' overall from 2019 to 2021?
* how did 'Inflection Point Ventures' rank in 2020 in terms of most 'Company/Brand' funded?
* which city received the highest Avg. Rating score? How many Companies Funded are there?
* which city stands out in terms of total funding received by companies and salary paid to their employees (with scatterplot)?

In ```diamonds_taxis``` notebook, I plotted six charts to show some of my skills with Pandas and Seaborn.  

About diamonds:
* bar chart showing average price per clarity and average carat per clarity
* jointplot showing the relationship between carat and price per clarity  

About taxis:
* barchart showing number of rides for each day of the week and number of rides per hour if the day
* barplot showing rides per hour on Friday
* barcharts showing average tip_pct by dropoff_borough and, on the right, average absolute tip
* scatterplot showing relationship between fare and tip

### Thanks for reading!