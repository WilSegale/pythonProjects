from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("")

# Extract the audio
audio = video.audio

# Save the extracted audio to a file
audio.write_audiofile("path/to/your/extracted_audio.wav")

