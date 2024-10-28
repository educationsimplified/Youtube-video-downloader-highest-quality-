from pytube import YouTube

# Introduction message
print("YouTube Video Downloader by Uzair")

# Ask the user to input the YouTube video link
video_url = input("Please enter the YouTube video link: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download(output_path="your_output_directory")

print("Download completed!")