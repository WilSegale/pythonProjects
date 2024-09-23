import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        print(f"Error getting public IP: {e}")
        return None

def is_connected_to_vpn(known_ip=None):
    current_ip = get_public_ip()
    if current_ip is None:
        return None
    
    if known_ip and current_ip != known_ip:
        return True
    else:
        # You might add logic to check if the IP belongs to a known VPN range.
        print(f"Your current public IP is: {current_ip}")
        return False

# Replace with your known non-VPN public IP
known_ip = "127.0.0.1"
if is_connected_to_vpn(known_ip):
    print("You are connected to a VPN.")
else:
    print("You are not connected to a VPN.")

