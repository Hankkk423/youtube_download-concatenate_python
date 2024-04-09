# Download & Concatenate Audio Files from YouTube in Python

Concatenating audio files is a common task in audio processing, and it can be done easily using Python. This repository shows how to concatenate audio files from a folder using the python module.

## Installation

Before running the code, ensure you have the required packages installed. You can install them using the `requirements.txt` file.

## Usage

1. Clone this repository to your local machine.
2. Install the required packages as mentioned in the installation section.

### Steps

1. Copy Paste the description with links to 'temp_description.txt'.
2. Run 'extractUrls.py' to extract the urls of '- Watch:' from 'temp_description.txt' to 'youtube_urls.txt'.
3. Run 'downloadAudio.py' to download audio files from the links in 'youtube_urls.txt'.
4. Run 'audioCombine(from a folder).py' to combine the audio files into one mp3 file.
5. You get a 'combined_audio.mp3' which is an all-in-one audio file.

### extractUrls.py

1. It'll extract every YouTube url started with '- Watch:' in 'temp_description.txt', and put it in 'youtube_urls.txt'.

### downloadAudio.py

1. Simply copy paste the YouTube URLs to 'youtube_urls.txt'. Or you get the urls by running 'extractUrls.py'.
2. Run the code and start downloading.

### audioCombine(from a folder).py

1. It'll combine the audio files in 'downloaded_audio' folder (generated by downloadAudio.py).
2. It'll generate 'combined_audio.mp3' in 'combined_audio' folder.

### audioCombine(from subfolders).py

1. Change the MAIN_FOLDER_PATH in 'constants.py'. It should be a main folder that contains many subfolders, each subfolder contains many audio files. For example, Main Folder -> Subfolder -> Audio files. 

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes and push them to your fork.
5. Create a pull request to the original repository.

## License

This project is licensed under the MIT License. You can find more details in the LICENSE file.

## Trobule Shooting

### downloadAudio.py

The error message, `FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe'`, indicates that `pydub` is unable to locate `ffprobe`, which is one of the required dependencies for audio file processing.

To resolve this issue, you need to ensure that `ffprobe` is installed and accessible on your system. `ffprobe` is part of the FFmpeg package, which is commonly used for audio and video processing.

Here are the steps to install FFmpeg on macOS using Homebrew:

1. Open Terminal.
2. Install Homebrew if you haven't already. You can install Homebrew by running the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Once Homebrew is installed, use the following command to install FFmpeg:

```bash
brew install ffmpeg
```

After installing FFmpeg, you need to ensure that `ffprobe` is accessible in your system's PATH. You can verify this by running `ffprobe` in Terminal. If `ffprobe` is correctly installed and accessible, you should see its usage information.

Once `ffprobe` is installed and accessible, rerun your Python script, and the error should be resolved.