import googleapiclient.discovery
import downloader
import uploader

print("[+]Script Starting...")

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

print("[+]Found a trending short!")

print("[+]Id and title is "+id+" "+title)

print("[+]Downloading video...")

downloader.download(id)
print("[+]Downloaded video file with audio!")

uploader.upload(str(id+".mp4"),title)
print("[+]Upload completed!")
print("[+]Terminating...")
exit()
