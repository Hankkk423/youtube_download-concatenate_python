from pydub import AudioSegment
from tqdm import tqdm
import os
import shutil


def concatenate_audio_pydub(audio_clip_paths, output_path, verbose=1):
    """
    Concatenates audio clips specified by `audio_clip_paths` into one audio file and saves it to `output_path`.
    """
    def get_file_extension(filename):
        """A helper function to get a file's extension"""
        return os.path.splitext(filename)[1].lstrip(".")

    clips = []
    audio_clip_paths = tqdm(audio_clip_paths, "Reading audio file") if verbose else audio_clip_paths
    for clip_path in audio_clip_paths:
        extension = get_file_extension(clip_path)
        clip = AudioSegment.from_file(clip_path, extension)
        clips.append(clip)

    # Concatenate all audio clips into a single clip
    final_clip = sum(clips)

    final_clip_extension = get_file_extension(output_path)
    if verbose:
        print(f"Exporting resulting audio file to {output_path}")
    final_clip.export(output_path, format=final_clip_extension)

def collect_audio_files(folder_path):
    """
    Collects all MP3 files from the specified folder.
    """
    mp3_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            mp3_files.append(os.path.join(folder_path, file))
    return mp3_files

def main():
    # Specify the path to the folder containing all the audio files
    audio_folder_path = "downloaded_audio"

    # Collect all MP3 files from the audio folder
    mp3_files = collect_audio_files(audio_folder_path)

    print("mp3_files", len(mp3_files))

    # Specify the output path for the combined audio file
    output_path = "combined_audio/combined_audio.mp3"

    # Folder to save combined audio file
    output_folder = "combined_audio"

    # Check if the output folder exists
    if os.path.exists(output_folder):
        # If it exists, delete it and recreate it
        shutil.rmtree(output_folder)
    # Create the output folder
    os.makedirs(output_folder)

    # Combine the audio files
    concatenate_audio_pydub(mp3_files, output_path, verbose=1)

if __name__ == "__main__":
    main()
