import requests

try:
    response = requests.get("https://www.google.com")
    response.raise_for_status()
    print("The internet is up!")
except requests.exceptions.RequestException as e:
    print("The internet is down!")

