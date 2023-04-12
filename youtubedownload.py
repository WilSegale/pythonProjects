from pytube import YouTube
from colorama import *

GREEN = Fore.GREEN #works correctly
RESET = Fore.RESET #resets the color 

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    
    print(f"{GREEN}Download is completed successfully{RESET}")

link = input("Enter the YouTube video URL: ")
Download(link)