#!/usr/bin/env python
# coding: utf-8

# # Data Scrapping of #NigeriaDecides2023, #2023Elections and #SOSREX twitter hashtags which are on the Nigerian Presidential Elections.
# This code snippet retrieves the latest tweets containing the #SOSREX hashtag using the sntwitter package 
# It creates a pandas dataframe Tweets_data with columns for the date, username, display name, tweet content, number of likes, 
#number of retweets, source of tweet, number of followers, and location.

# 
# All codes are written in the python using the following libraries: snscrape, datetime, and pandas

# In[1]:


#importing the necessary libraries needed for scrapping
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime, time
from datetime import timedelta


# In[13]:


#Format since and until timestamps for Twitter API


query= '(NigeriaDecides2023) lang:en until:2023-02-27 since:2023-02-17'


# In[14]:


Election_tweets=[]


# In[16]:


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(Election_tweets)>5000:
        break
    else:
        Election_tweets.append([tweet.date,tweet.user.username,tweet.user.displayname,tweet.url,
                            tweet.content,tweet.likeCount,tweet.retweetCount,
                            tweet.quoteCount,
                            tweet.sourceLabel,tweet.user.followersCount,tweet.user.location
                           ])
    
# Creating a dataframe from the tweets list above 
Election_data = pd.DataFrame(Election_tweets, 
                         columns=["Date_tweeted","username","display_name","tweet_link", 
                                  "Tweets","Number_of_Likes","Number_retweets",
                                  "Qouted_times",
                                  "Source_of_Tweet",
                                  "number_of_followers","location"
                                 ])



#removing the "+00:00" in the datetime
Election_data["Date_tweeted"]=pd.to_datetime(Election_data['Date_tweeted']).dt.strftime('%Y-%m-%d %H:%M:%S')

#Exporting the data to the repository as csv

import os
# Load the existing data into a DataFrame
filename = "Election_data.csv"
existing_data = pd.read_csv(filename)

# Append the new data to the existing data (assuming it has the same columns)
new_data = Election_data  # Replace with the code to scrape and store the new data
if len(new_data.columns) == len(existing_data.columns):
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    # Drop duplicate rows and write the combined data back to the same file
    combined_data.drop_duplicates(inplace=True)
    combined_data.to_csv(filename, index=False)
else:
    print("The new data has a different number of columns than the existing data.")



