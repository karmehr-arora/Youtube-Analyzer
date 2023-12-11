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
views, likes, and comments. It can organize 
the data to compare their performances. Once it 
gathers the data, it can plot datas into graphs to 
visualize the datas. With the help of interface, 
people can visualize better and make better 
decisions which YouTube videos are trending.

## Project Outline/Plan

### Interface Plan
    We can use tkinter to display the interface by gathering 
    the data to determine the audience's expectations. We 
    could navigate system in user-friendly manner.
    
### Data Collection and Storage Plan (Author #1)
    For data collection, we plan to access the data through YouTube's API. Using this, we can access all the 
    likes, comments, dislikes, tags, etc. from a video and then store and analyze this data.
    For data storage we plan to not store the data as our application can run without the use of data storage. Data will 
    only be retrieved through YouTube API and will be refreshed on every search the user makes.

### Data Analysis and Visualization Plan (Author #2)
    Our group plans to analyze the data in a way that we can understand the most trending videos in a certain time period 
    (for example by looking at the number of views in that time period) or the most liked videos of the day, etc. We plan on 
    presenting these videos using a graph and a table with links to each of the videos. This will be done using tkinter and python

### Installation Instructions
    To install the project, all you have to do is install the python and jupyter notebook files, install the required libraries 
    the application imports in, and then insert your own Youtube API key.  Then you can run the GUI file and the Youtube Analyzer
    should work just as expected.

### Future Updates
    In the future, if we were to continue working on the project in another class, we would hyperlink the links for each video 
    so that, when they are clicked on, they will take you directly to the video. This would be instead of having to copy paste 
    the links. Another change we would make is that we would number the videos to show to the user that the videos are sorted 
    from most trending to least trending.
