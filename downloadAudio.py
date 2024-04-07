from pytube import YouTube
from pydub import AudioSegment
import os
import ssl 

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

def download_and_convert_audio(youtube_urls, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for url in youtube_urls:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        
        # Download the audio file as MP4
        mp4_file = video.download(output_path=output_folder)

        # Convert MP4 to MP3
        mp3_file = os.path.join(output_folder, f"{yt.title}.mp3")
        AudioSegment.from_file(mp4_file).export(mp3_file, format="mp3")

        # Remove the downloaded MP4 file
        os.remove(mp4_file)

        # Print result of success
        print(f"{yt.title} has been successfully downloaded and saved as MP3 in {output_folder}")


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

# Download and convert audio files
download_and_convert_audio(youtube_urls, output_folder)
