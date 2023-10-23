import googleapiclient.discovery

print("Script Starting...")

# Replace with your own API key
api_key = "AIzaSyCESfsBQ4nBrHQ0TwsLleMWrXazpinNZVM"

# Create a YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Request the trending videos
request = youtube.search().list(
    part="snippet",
    q="",
    maxResults=10,  # You can change the number of results you want
    type="video",
    videoDuration="short",
    regionCode="IN",  # You can change this to your desired region code
)



resp = request.execute()["items"][0]
id=resp["id"]["videoId"]
title = resp["snippet"]["title"]


print(id,title)