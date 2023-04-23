from pytube import YouTube
import os
from moviepy.editor import *

# Input YouTube link
link = input("Enter the YouTube link: ")

# Create a YouTube object
yt = YouTube(link)

# Get the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()

# Download the audio stream to a file
audio_file = audio_stream.download()

# Convert the audio file to MP3 format
audio_clip = AudioFileClip(audio_file)
audio_clip.write_audiofile("output.mp3")

# Delete the original audio file
os.remove(audio_file)

