# CS122_Final_Project
This is the final project for CS 122 Advanced Python


## Project Title:
YouTube Analyzer

## Authors
Karmehr Arora, Alfred Koh

## Project Description (5 Sentences)
YouTube Analyzer is a project provide users 
with insights and analyzing their performances.
It can access the data and analyze the metrics like
views, likes, subscribers. It can organize 
the data to compare their performances. Once it 
gathers the data, it can plot datas into graphs to 
visualize the datas. With the help of interface, 
people can visualize better and make better 
decisions which YouTube videos are trending.

## Project Outline/Plan

### Interface Plan
    We can use flask to display the interface by gathering 
    the data to determine the audience's expectations. We 
    could navigate system in user-friendly manner. We also could
    provide a dashboard for an overview of their performances.
    
### Data Collection and Storage Plan (Author #1)
    For data collection, we plan to access the data through YouTube's API. Using this, we can access all the 
    likes, comments, dislikes, tags, etc. from a video and then store and analyze this data.
    For data storage we plan to store the data in either a set of database tables or a spreadsheet. It's still 
    to be determined what data we need to store and for how long as the data is readily available through YouTube API.

### Data Analysis and Visualization Plan
    Our group plans to analyze the data in a way that we can understand the most trending videos in a certain time period 
    (for example by looking at the number of views in that time period) or the most liked videos of the day, etc. We plan on 
    presenting these videos using a graph and a table with links to each of the videos. This will be done using flask and python