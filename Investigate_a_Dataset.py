#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: TMDB 5000 Movie Dataset
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# #### This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
# <ul>
# 
# <li>Certain columns, like ‘cast’
# and ‘genres’, contain multiple
# values separated by pipe (|)
#     characters.</li>
# <li>There are some odd characters
# in the ‘cast’ column. Don’t worry
# about cleaning them. You can
# leave them as is.</li>
# <li>The final two columns ending
# with “_adj” show the budget and
# revenue of the associated movie
# in terms of 2010 dollars,
# accounting for inflation over
# time.</li>
# </ul>
# 
# In terms of questions that can be explored from this data, my analysis is based on how  popularity, vote counts and release year affect revenue collection.

# In[1]:


# Use this cell to set up import statements for all of the packages that you
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, I will load in the data, check for cleanliness, and then trim and clean your dataset for analysis.
# 
# ### General Properties

# In[2]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv('tmdb-movies.csv')
df.head(3)


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


df.info()


# 
# ### Data Cleaning (Replace this with more specific notes!)
# 
# In terms of data cleaning, I see that the existing data is clean enough, but there are some columns which I think will not help me in the data analysis process, so I will delete these columns(id , imdb_id  and homepage ) .

# In[6]:


df.drop(['id', 'imdb_id','homepage'], axis = 1, inplace = True)


# In[7]:


df.head(5)


# In[8]:


df.info()


# Because the column(genres) is an essential feature for parsing, and now it has some missing data, so I'm going to drop the missing data.
# <br><br>
# But before dropping the missing data, I will fill in the missing data for each of these features(cast,director, tagline, keywords, overview and production_companies )

# In[9]:


df.fillna(value = {'cast':'unknown'
                                ,'director':'unknown'
                                ,'tagline':'unknown'
                                ,'keywords':'unknown'
                                ,'overview':'unknown'
                                ,'production_companies':'unknown'}
          
          ,inplace=True)
df.info()


# In[10]:


df.dropna(inplace=True)
df.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# ### Research Question  (what are movies genres have the highest votes ?)

# In[11]:


def AvgRev(x):
    median = x.median()
    
    low  = df[x <  median]
    high = df[x >= median]
    

    mean_revenue_low = low['revenue'].mean()
    mean_revenue_high = high['revenue'].mean()
    
    colors = ['red', 'blue']
    locations = [1, 2]
    heights = [mean_revenue_low, mean_revenue_high]
    labels = ['Low', 'High']
    return (locations, heights, labels, colors)


# In[12]:


locations,heights,labels, colors = AvgRev(df['popularity'])  

plt.bar(locations, heights, tick_label=labels,  color = colors)
plt.title('Average Revenue by popularity')
plt.xlabel('ppopularity')
plt.ylabel('Average revenue')


# ####  It shows that there is a clear relationship between increased revenue and increased popularity. We note that the higher the popularity, the higher the revenue.

# In[13]:


locations,heights,labels, colors = AvgRev(df['vote_count'])  

plt.bar(locations, heights, tick_label=labels,  color = colors)
plt.title('Average Revenue by Vote Count')
plt.xlabel('vote count')
plt.ylabel('Average revenue');


# #### We note from the graph that there is a strong relationship between the increase in vote counts and the increase in revenues, as the increase in revenues depends largely on the increase in vote counts.

# In[14]:


plt.scatter(df["release_year"],df["revenue"])
plt.title(' Revenue Vs Release year')
plt.xlabel('release_year')
plt.ylabel('revenue');
plt.show()


# #### It also appears that the increase in revenues increases over time, as the revenues increase with the progression of the years as can be seen in the figure.

# <a id='conclusions'></a>
# ## Conclusions :
# 
# >In my analysis of the data of this project, I relied on the feature Revenue, we note that the increase the popularity, the increase the Revenue  and vice versa.
# 
# >We also note that the greater the number of votes on the movie, it leads to an increase in Revenue and vice versa
# 
# >We also note that the revenue increases very significantly with the increase of the release year
# 
# 
# ## limitations :
# 
# >To implement this project, I used a (TMDB Movie) dataset , and the analysis focused on popularity, Count of votes and year of release. My analysis is limited to the dataset presented only. For example, the dataset does not contain where movies are shown.
# 
# >There are several missing values ​​that may skew my analysis and may show an unintended bias towards the relationship being analyzed. Plus, it forced me to work harder on the data cleaning phase.

# In[15]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




