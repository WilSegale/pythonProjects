import requests
import time

url = "https://google.com"
file_size = 1024 * 1024  # Size of the file to download in bytes (1 MB in this case)

start_time = time.time()
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open("downloaded_file.html", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):  # Adjust chunk size as needed
            f.write(chunk)
else:
    print("Failed to download the file.")

end_time = time.time()

download_time = end_time - start_time
download_speed = file_size / download_time / 1024  # Speed in KB/s

print(f"Download speed: {download_speed:.2f} KB/s")

