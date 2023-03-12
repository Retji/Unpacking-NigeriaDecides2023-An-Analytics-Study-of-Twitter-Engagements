# Unpacking #NigeriaDecides2023: An Analytics Study of Twitter Engagements

![elections pic (2)](https://user-images.githubusercontent.com/37171086/222526531-b6d04b37-0d90-4b63-93b4-76cf0a188a99.png)



**Introduction**
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
**Data Sourcing**

During the data sourcing phase, I utilized Python with the snscrape library to continuously scrape Twitter data related to the Nigerian Presidential Election using the #NigeriaDecides2023 and #SOSREX hashtags. The resulting data was stored in a CSV file, which is hosted in this repository. To ensure a continuous stream of data,I utilized Github actions, with the YAML code for continuous integration located in the workflow directory.

---
**Data Cleaning and Transformation**

![data transformation](https://user-images.githubusercontent.com/37171086/223644925-7adc08af-f944-45a7-84b1-c0c3a5fd8ec2.png)

The data was pre-cleaned while it was being scraped. The 00.00 time component in the dataset was droped using python. The data was then loaded in PowerQuery using PowerBI. No column was dropped. However, three columns where added during the transformation process.
- *__Score sentiment column__* -this column gives a score of the tweet sentiment in the tweets column. This was possible using the cognitive service from text analysis feature
- *__Sentiment column__* -this is a conditional column base on the score sentiment column. Sentiment scored below 0.4 are considered Negative; sentiments with a score between 0.4 and 0.7 are considered Neutral whereas sentiments with score above 0.7 are Positive.
- *__Icons column__* -this column attaches an image url to emoji base on whether the sentiments are Negative, Neutral or Positive

---
**Visualization and Analysis**

![unpack viz](https://user-images.githubusercontent.com/37171086/223653085-2cab240a-19b5-4895-bf68-af746d7da8dc.png)


After visualization, these are the key insights:
1. 52% of the tweets were reported Neutral. These probably was due to language barrier while the text analytics AI conducted the score. A large volume of the dataset was in "pigin", Nigeria's widely spoken form of English;
2. A large number of tweets are coming from android users,65k of 122k tweets analyzed. Hence optimizing usage of android app for twitter should be a key consideration as most twitter users in Nigeria can be inferred to be adroid users;
3. Iphone users tend to have an above average Negative sentiment about Nigeria's election. With a 16% general score, Negative sentiment was 20% for iphone users;
4. The most liked tweets was about results declaration by Ekiti state. The first state to declare results was Ekiti state, this shows genuine enthusiasm and anxiety for the outcome of the elections;
5. The most re-tweeted tweet was about an alleged tweet on a video trending regarding the Nigerian Army interferrence and collusion to help rig the election.


You can interact and view the dashboard visualization [here:](https://app.powerbi.com/view?r=eyJrIjoiOTkxOGI4NmItN2JkZS00ZDk0LTk4ZmYtNDg5ZTFiNzg4YmVhIiwidCI6ImM4MzgxNmI2LWJhMjAtNGQ0Mi05YzQyLWFiMzAyODczOTM5MSJ9&pageName=ReportSection8eded047b1738d111570)


---
**Disclamer and Issues**

This repository is still a work in progress, updates on data and dashboard may change as more data comes in. There are known issues with the Yaml code in the branch which was meant to continously scrape and update the data, which is being tackled. 

