import subprocess

def upload(video_file,video_title):

	video_description = "#endmeme"
	video_category = "22"  # Change to the desired category
	privacy_status = "public"  # Choose from "public", "private", or "unlisted"

	# Execute the YouTube video upload script with the specified arguments
	command = [
	    "python",  # Use "python" or "python3" based on your Python installation
	    "test.py",  # Replace with the actual filename of your YouTube upload script
	    "--file", video_file,
	    "--title", video_title,
	    "--description", video_description,
	    "--category", video_category,
	    "--privacyStatus", privacy_status,
	]

	subprocess.run(command)

