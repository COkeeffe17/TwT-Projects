# Youtube video downloader. Actually had to use yt_dlp rather than pytube as pytube does not work with the new youtube system, but other than that copied directly from TwT's video, as I had no idea how to use filedialog.

import yt_dlp
import tkinter as tk
from tkinter import filedialog


# Downloading the video
def download_video(url, save_path):
    ydl_opts = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save with video title
        "format": "best",  # Choose best quality
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Video downloaded successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


# Folder
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


# Inputs
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a YouTube url:   ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location ")

    else:
        download_video(video_url, save_dir)
