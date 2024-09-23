from DontEdit import *
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print(F"{RED}[-] An error has occurred")
    
    print(GREEN + "Downloading video: " + RESET + youtubeObject.title)

link = input("Enter the YouTube video URL: ")
Download(link)