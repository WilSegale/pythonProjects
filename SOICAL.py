import requests
from bs4 import BeautifulSoup
print("input the username")
username = input(">>> ")
print("input the site")
site = input(">>> ")
url = f"{site}{username}"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Check if the profile exists by looking for a "Not found" message on the page
not_found = soup.find("div", class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
if not_found:
    print("Profile not found.")
else:
    print(f"Profile found: {url}")
