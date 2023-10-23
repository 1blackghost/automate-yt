from pytube import YouTube

def download(video_id):

	# Replace with the video ID of the YouTube Short

	# Create a YouTube object
	url = f"https://www.youtube.com/watch?v={video_id}"
	yt = YouTube(url)

	# Get the stream with the highest resolution that includes both video and audio
	stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

	# Set the output directory and filename
	output_dir = "."  # Change this to your preferred directory
	output_file = f"{video_id}.mp4"

	# Download the video
	stream.download(output_path=output_dir, filename=output_file)

	print(f"Video with video ID {video_id} downloaded successfully.")
