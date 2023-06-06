from pytube import YouTube
from colorama import *

GREEN = Fore.GREEN #works correctly
RESET = Fore.RESET #resets the color 
RED = Fore.RED # color for the error message

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