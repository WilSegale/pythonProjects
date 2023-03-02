import requests
username = input(">>> ")
snap = f'https://www.snapchat.com/add/{username}'

site={f"{snap}"}
response = requests.post(site, data=username)

if response.status_code == 200:
    html = response.text
    print(f"site found {site}")