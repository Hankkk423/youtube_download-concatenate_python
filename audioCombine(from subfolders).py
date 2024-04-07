from pydub import AudioSegment
from tqdm import tqdm
import os
import constants

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

    final_clip = clips[0]
    range_loop = tqdm(list(range(1, len(clips))), "Concatenating audio") if verbose else range(1, len(clips))
    for i in range_loop:
        final_clip = final_clip + clips[i]

    final_clip_extension = get_file_extension(output_path)
    if verbose:
        print(f"Exporting resulting audio file to {output_path}")
    final_clip.export(output_path, format=final_clip_extension)

def collect_audio_files(folder_path):
    """
    Collects all MP3 files from subfolders within the specified folder.
    """
    mp3_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def main():
    # Specify the path to the main folder containing subfolders with audio files
    main_folder_path = constants.MAIN_FOLDER_PATH

    # Collect all MP3 files from subfolders
    mp3_files = collect_audio_files(main_folder_path)

    # Specify the output path for the combined audio file
    output_path = "combined_audio/combined_audio.mp3"

    # Create the output folder if it doesn't exist
    if not os.path.exists("combined_audio"):
        os.makedirs("combined_audio")

    # Combine the audio files
    concatenate_audio_pydub(mp3_files, output_path, verbose=1)

if __name__ == "__main__":
    main()
