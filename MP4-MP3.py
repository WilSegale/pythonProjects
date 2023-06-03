from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("/Users/admin/Desktop/github/pythonProjects/apache.mp4")

# Extract the audio
audio = video.audio

# Save the extracted audio to a file
audio.write_audiofile("extracted_audio.mp3")
