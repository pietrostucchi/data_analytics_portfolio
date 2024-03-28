# SQL Analysis - European Soccer Database

## Summary of Project

With this project, I would like to show my skills in using SQL: calculations with operators, joins, union operator, Data Definition Language, Data Manipulation Language, subqueries, window functions.

I will query some tables of the European Soccer Database, which holds informations about matches, leagues, players and teams attributes for European Professional Football.

You can find the tables in the European Soccer Database folder as a collection of four individual csv files:
* leagues.csv
* match.csv
* player.csv 
* team.csv

The schema of the relationships between these four tables at this [LucidChart link](https://lucid.app/lucidchart/4207f1c5-49cd-4c6c-b0ab-6ec904dbedef/edit?viewport_loc=-934%2C-186%2C1813%2C743%2C0_0&invitationId=inv_3523cced-c79f-4438-87cd-ba59a218d87a).

Instead, the entire database is public and can be found on [Kaggle](https://www.kaggle.com/datasets/hugomathien/soccer).

I made this project uploading the csv files on Google BigQuery.

## Files

```european_soccer.sql```: queries to answer to each question  
```european_soccer_database```: csv data folder

## Informations to retrieve

I wanted to answer the following questions:

1. How many days have passed from the oldest Match to the most recent one (dataset time interval)?

2. For each season and league name, show the following statistics about the home goals scored: 
    * min
    * average 
    * mid-range 
    * max 
    * sum  

    Which combination of season-league has the highest number of goals? 

3. How many unique seasons there are in the match table?

4. For each season, what's the number of matches played by each League?

5. Using players as the starting point, create a new table (player_BMI) and: 
    * add a variable that represents the players' weight in kg (from pounds) and call it kg_weight; 
    * add a variable that represents the height in metres (from cm) and call it m_height; 
    * add a variable that shows the body mass index (BMI) of the player;
    * filter the table to show only the players with an optimal BMI (from 18.5 to 24.9).

6. How many players do not have an optimal BMI?

7. Which team has scored the highest total number of goals (home + away) during the most recent available season? How many goals has it scored? 

8. For each season, show the name of the team that ranks first in terms of total goals scored. Which team was the one that ranked first in most of the seasons? 

9. Create a new table (top_scorer) containing the top 10 teams in terms of total goals scored. Then write a query that shows all the possible "pair combinations" between those 10 teams. How many "pair combinations" did it generate? 


### Thanks for reading!

