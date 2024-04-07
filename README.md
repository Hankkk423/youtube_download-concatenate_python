# Download & Concatenate Audio Files from YouTube in Python

Concatenating audio files is a common task in audio processing, and it can be done easily using Python. This repository shows how to concatenate audio files from a folder using the python module.

## Installation

Before running the code, ensure you have the required packages installed. You can install them using the `requirements.txt` file.

## Usage

1. Clone this repository to your local machine.
2. Install the required packages as mentioned in the installation section.

### downloadAudio.py

1. Simply copy paste the YouTube URLs in 'youtube_urls.txt'.
2. Run the code and start downloading.

### audioCombine(from a folder).py

1. It'll combine the audios in 'downloaded_audio'

### audioCombine(from subfolders).py

1. Change the MAIN_FOLDER_PATH in 'constants.py'. It should be a main folder that contains many subfolders, each subfolder contains many audio files.

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