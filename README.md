# Unpacking #NigeriaDecides2023: An Analytics Study of Twitter Engagements

![elections pic (2)](https://user-images.githubusercontent.com/37171086/222526531-b6d04b37-0d90-4b63-93b4-76cf0a188a99.png)



Introduction
---
Welcome to the README file for the Analytics of #NigeriaDecides2023 Twitter Engagements. This document provides a detailed overview of the data analysis performed on Twitter engagements while the election process was going on.

Social media platforms like Twitter have become essential tools for political campaigns and a source of information for voters, and as such, understanding the sentiments and behaviors of users during election periods is crucial for gaining insights into public opinion.

This analysis is designed to provide an in-depth look at the Twitter engagements related to #NigeriaDecides2023, including metrics such as tweet volume, sentiment analysis, hashtag usage, and user engagement. By examining these metrics, we hope to provide a comprehensive understanding of the online conversations around the Nigerian general election and contribute to a broader understanding of public opinion in Nigeria.

I hope that the information provided in this analysis will be useful for journalists, politicians, and researchers who are interested in studying social media and its impact on elections.

This report is in two parts:
1. Data gathering and cleaning
2. Data visualization and reporting on PowerBI

---
**Problem statement**

The objective of this study is to collect and analyze Twitter data related to the Nigerian Presidential Election using the #NigeriaDecides2023 and #SOSREX hashtags. The analysis will involve visualizing the data and conducting sentiment analysis on the text to gauge public sentiment regarding the election.

---
Data Sourcing
During the data sourcing phase, I utilized Python with the snscrape library to continuously scrape Twitter data related to the Nigerian Presidential Election using the #NigeriaDecides2023 and #SOSREX hashtags. The resulting data was stored in a CSV file, which is hosted in this repository. To ensure a continuous stream of data,I utilized Github actions, with the YAML code for continuous integration located in the workflow directory.

---
**Data Cleaning and Transformation**
![data transformation](https://user-images.githubusercontent.com/37171086/223644925-7adc08af-f944-45a7-84b1-c0c3a5fd8ec2.png)

The data was pre-cleaned while it was being scraped. The 00.00 time component in the dataset was droped using python. The data was then loaded in PowerQuery using PowerBI. No column was dropped. However, three columns where added during the transformation process.
- Score sentiment column-this column gives a score of the tweet sentiment in the tweets column. This was possible using the cognitive service from text analysis feature
- Sentiment column-this is a conditional column base on the score sentiment column. Sentiment scored below 0.4 are considered Negative; sentiments with a score between 0.4 and 0.7 are considered Neutral whereas sentiments with score above 0.7 are Positive.
- Icons column-this column attaches an image url to emoji base on whether the sentiments are Negative, Neutral or Positive

---
This code snippet retrieves the latest tweets containing the #NIGERIADECIDES2023 hashtag using the sntwitter package and creates a pandas dataframe Tweets_data with columns for the date, username, display name, tweet content, number of likes, number of retweets, source of tweet, number of followers, and location. To view the resulting dataframe, you can simply run Tweets_data after the code snippet. Here's the code snippet displaying the resulting dataframe. All codes are written in the python using the following libraries: snscrape, datetime, and pandas
