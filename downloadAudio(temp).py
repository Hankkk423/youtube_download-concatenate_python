from pytube import YouTube
import os
import ssl # Import SSL module

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

# # List of YouTube URLs
# youtube_urls = [
#     # Add YouTube URLs here
#     "https://www.youtube.com/LINK-1",
#     "https://www.youtube.com/LINK-2",
# ]

# Read YouTube URLs from "youtube_urls.txt" file
youtube_urls_file = "youtube_urls.txt"
with open(youtube_urls_file, 'r') as file:
    youtube_urls = file.readlines()
youtube_urls = [url.strip() for url in youtube_urls if url.strip()]  # Remove empty lines and strip whitespace

# Folder to save downloaded audio files
output_folder = "downloaded_audio"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for url in youtube_urls:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    
    # Destination directory
    destination = output_folder  # Use output folder
    # Download the file
    out_file = video.download(output_path=destination)

    # Save the file as MP3
    base, ext = os.path.splitext(out_file)
    new_file = os.path.join(destination, f"{yt.title}.mp3")
    os.rename(out_file, new_file)

    # Print result of success
    print(yt.title + " has been successfully downloaded and saved in " + output_folder)
