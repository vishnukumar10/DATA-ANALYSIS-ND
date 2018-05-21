"""Project: Investigating the TMDb Movie Dataset.
Table of Contents
->Introduction
->Data Wrangling
->Exploratory Data Analysis
->Conclusions

Introduction
The chosen topic for Analysing the data is TMDb Movie dataset. It consists of a complete detailed list of the movie including the popularity, revenue, casting details and so on. 
The main question asked about a movie in the perspective of the movie producer is how popular a movie has become and mainly how much money it has grossed as its revenue. 
These two will be the main focus in the analysis below.
"""

# Importing Libraries
​
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
​

"""
Data Wrangling
General Properties
"""

#Loading Data
​
df = pd.read_csv('movies.csv')
df.head()
df.describe()  	
df.info()

"""
Data Cleaning
The main focus is to analyse the popularity of the Film, So a few not very relavent columns are dropped. They include imdb_id, Cast,Home Page, Tagline, Overview, 
Production Company and Release Date.

There are not any NULL values obtained after the columns have been dropped. So we move to Exploring the Data and Analysing it.
"""


#Dropping Columns
df.drop(['imdb_id','cast','homepage','director','tagline','overview','production_companies','release_date','keywords','release_year','genres','budget_adj','revenue_adj'],axis=1,inplace=True)
df.head()


#Exploratory Data Analysis


"""
How does Popularity depend upon other Columns?
The Main Goal of this section is to compare and contrast the Popularity Column.
We will compare the Popularity column to the other columns and try to find corelations between them and represent visuals for it
"""


df.groupby('budget').popularity.mean().plot(kind='line',figsize=(8,8))

df.groupby('vote_average').popularity.mean().plot(kind='line',figsize=(8,8))

df.groupby('revenue').popularity.mean().plot(kind='line',figsize=(8,8))

df.groupby('vote_count').popularity.mean().plot(kind='line',figsize=(8,8))





"""
How does Revenue depend upon other Columns?
The Main Goal of this section is to compare and contrast the Popularity Column.
We will compare the Popularity column to the other columns and try to find corelations between them and represent visuals for it
"""

df.groupby('budget').revenue.mean().plot(kind='line',figsize=(8,8))

df.groupby('vote_average').revenue.mean().plot(kind='line',figsize=(8,8))

df.groupby('vote_count').revenue.mean().plot(kind='line',figsize=(8,8))

df.groupby('popularity').revenue.mean().plot(kind='line',figsize=(8,8))




"""

Conclusions:
There are a few important conclusion drawn from the dataset that was provided. The popularity of the movie has a positive corelation with four key factors they are,
the Budget, the revenue, the vote count and the vote average. This means that the popularity of the film increases with the increase in budget, revenue and so on. 
And next, the revenue of the movie. That is, how much the movie has grossed in its theatrical run. This also has a positive corelation on the following factors, 
the budget, the vote average, the vote count and the popularity.

Limitations: One of the main limitations of the this exploration is the inability to consider the directors and the casting. Very often, we know that the 
casting plays a crucial role in the popularity of the film, the more popular the actor is, the more popular the movie is. But this factor could not be taken into the analysis.

"""