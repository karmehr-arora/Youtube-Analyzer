# @author Karmehr Arora
# import utilized libraries pertaining to data collection
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from datetime import datetime
from datetime import timedelta

# method to get topic from UI
def search(search_bar):
    topic = search_bar.get()
    if(len(topic) == 0):
        topic = ""
    return topic

def getDate(ageInDays):
    current_datetime = datetime.now() - timedelta(days=ageInDays)
    return current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

def daysAge(input):
    date = datetime.strptime(input, '%Y-%m-%dT%H:%M:%SZ')
    current_datetime = datetime.now()
    # Calculate difference between the current date and the given date
    difference = (current_datetime - date).days
    return difference

# make a request to the api to find videos under that topic
# note: cost of this operation is 100 units of the alloted 10,000 units per 24 hours
def getVideos(modified_dt, topic, youtube):
    request = youtube.search().list(
            part="id,snippet",
            maxResults=50,
            publishedAfter=modified_dt,
            q=topic
        )
    return request.execute()


# collect & save videoIDs
def populateVideoIDs(videos):
    videoIDs = []
    for video in videos:
        if('videoId' in video['id']):
            videoIDs.append(video['id']['videoId'])
    return videoIDs

def collectVideoData(videos, youtube):
    collection_of_video_data = {}
    for video in videos:
        if('videoId' in video['id']):
            request = youtube.videos().list(part = 'snippet, statistics', id = video['id']['videoId'])
            response = request.execute()
            collection_of_video_data[video['id']['videoId']] = response
    return collection_of_video_data


def collectTrendData(collection_of_video_data):
    set_of_trend_totals = []
    for vid_data in collection_of_video_data:
        trendTotal = 0
        if "viewCount" in collection_of_video_data[vid_data]['items'][0]['statistics']:
            views = collection_of_video_data[vid_data]['items'][0]['statistics']['viewCount']
            trendTotal = trendTotal + int(views)
        if "likeCount" in collection_of_video_data[vid_data]['items'][0]['statistics']:
            likes = collection_of_video_data[vid_data]['items'][0]['statistics']['likeCount']
            trendTotal = trendTotal + int(likes)
        if "commentCount" in collection_of_video_data[vid_data]['items'][0]['statistics']:
            comments = collection_of_video_data[vid_data]['items'][0]['statistics']['commentCount']
            trendTotal = trendTotal + int(comments)

        set_of_trend_totals.append(trendTotal)
        return set_of_trend_totals


def matchVideoIDToTrendTotal(videoIDs, set_of_trend_totals):
    video_id_to_trend_total = {}
    count = 0
    for video in videoIDs:
        video_id_to_trend_total[video] = set_of_trend_totals[count]
        count = count + 1
    return video_id_to_trend_total

def getThumbnail(video):
    return video['snippet']['thumbnails']['high']['url']

def sortVideos(video_id_to_trend_total):
    return sorted(video_id_to_trend_total.items(), key=lambda x: x[1], reverse=True)[:10]