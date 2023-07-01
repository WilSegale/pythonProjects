from moviepy.editor import VideoFileClip

# Load the video file
print("Input the audio file")
video = VideoFileClip(input(">>> "))

# Extract the audio
audio = video.audio

# Save the extracted audio to a file
audio.write_audiofile("extracted_audio.mp3")
