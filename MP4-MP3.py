import ffmpeg

input_file = "input.mp4"
output_file = "output.mp3"

stream = ffmpeg.input(input_file)
audio_stream = stream.audio
audio_stream = ffmpeg.output(audio_stream, output_file)
ffmpeg.run(audio_stream)
